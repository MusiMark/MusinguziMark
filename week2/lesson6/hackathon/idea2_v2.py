"""
PERSON 1 – Entity Base Class & Treasure
Responsibility: Define the root Entity class that all game objects
inherit from, plus the Treasure subclass that ends the game.
"""


class Entity:
    """
    Base class for every object on the grid.
    All entities have a position (x, y) and a display symbol.
    """

    def __init__(self, x: int, y: int, symbol: str):
        self._x = x
        self._y = y
        self._symbol = symbol

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def symbol(self) -> str:
        return self._symbol

    def get_position(self) -> tuple[int, int]:
        return (self._x, self._y)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self._x}, y={self._y})"


class Treasure(Entity):
    """
    The goal of the maze.
    When the player steps on this tile the game is won.
    """

    def __init__(self, x: int, y: int):
        super().__init__(x, y, symbol="T")

    def collect(self) -> str:
        return "✨ You found the treasure! YOU WIN! ✨"
    
"""
PERSON 2 – Player Class
Responsibility: The Player entity with health, movement via WASD,
and boundary enforcement on a 5×5 grid.
"""

GRID_SIZE = 5

# Maps WASD keys to (dx, dy) deltas  (y increases downward)
MOVE_MAP = {
    "w": (0, -1),   # up
    "s": (0,  1),   # down
    "a": (-1, 0),   # left
    "d": (1,  0),   # right
}


class Player(Entity):
    """
    The human-controlled character.
    Starts with 3 health points; traps reduce health by 1.
    """

    MAX_HEALTH = 3

    def __init__(self, x: int, y: int):
        super().__init__(x, y, symbol="@")
        self._health: int = self.MAX_HEALTH

    # ── Health ────────────────────────────────────────────────
    @property
    def health(self) -> int:
        return self._health

    def take_damage(self, amount: int = 1) -> None:
        self._health = max(0, self._health - amount)

    def is_alive(self) -> bool:
        return self._health > 0

    # ── Movement ──────────────────────────────────────────────
    def move(self, key: str) -> bool:
        """
        Attempt to move the player in the direction of `key`.
        Returns True if the move was valid, False if blocked by wall.
        """
        key = key.lower()
        if key not in MOVE_MAP:
            return False

        dx, dy = MOVE_MAP[key]
        new_x = self._x + dx
        new_y = self._y + dy

        # Enforce grid boundaries
        if not (0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE):
            return False

        self._x = new_x
        self._y = new_y
        return True

    # ── Display helpers ───────────────────────────────────────
    def health_bar(self) -> str:
        filled = "♥ " * self._health
        empty  = "♡ " * (self.MAX_HEALTH - self._health)
        return (filled + empty).strip()

    def __repr__(self) -> str:
        return f"Player(x={self._x}, y={self._y}, hp={self._health})"
    
"""
PERSON 3 – Trap Class & Collision Detection
Responsibility: Define Trap entities and the CollisionDetector helper
that checks what the player has stepped on each turn.
"""


class Trap(Entity):
    """
    A hazard tile on the grid.
    Stepping on it reduces the player's health by 1.
    Active traps are visible; disarmed ones show a warning mark.
    """

    def __init__(self, x: int, y: int):
        super().__init__(x, y, symbol="X")
        self._active = True

    @property
    def is_active(self) -> bool:
        return self._active

    def trigger(self, player: Player) -> str:
        """Apply damage to player and deactivate trap."""
        if not self._active:
            return ""
        player.take_damage(1)
        self._active = False
        self._symbol = "!"    # Visual cue: trap has been triggered
        msg = f"💥 You hit a trap! Health: {player.health_bar()}"
        if not player.is_alive():
            msg += "\n💀 You have been defeated. GAME OVER."
        return msg


class CollisionDetector:
    """
    Checks the player's current position against every entity on the
    board and returns the result of any interaction.
    """

    @staticmethod
    def check(player: Player,
              traps: list[Trap],
              treasure: Treasure) -> dict:
        """
        Returns a dict:
            {
              "hit_trap":     Trap | None,
              "hit_treasure": bool,
              "message":      str,
            }
        """
        pos = player.get_position()
        result = {"hit_trap": None, "hit_treasure": False, "message": ""}

        # Check treasure first (win condition)
        if treasure.get_position() == pos:
            result["hit_treasure"] = True
            result["message"] = treasure.collect()
            return result

        # Check traps
        for trap in traps:
            if trap.get_position() == pos and trap.is_active:
                result["hit_trap"] = trap
                result["message"]  = trap.trigger(player)
                return result

        return result
    
"""
PERSON 4 – Grid Renderer
Responsibility: Draw the 5×5 maze to the terminal in a clean,
readable format every game turn.
"""

GRID_SIZE   = 5
EMPTY_CELL  = "."
H_BORDER    = "+" + "---+" * GRID_SIZE
HIDDEN_TRAP = "."     # Traps are hidden until triggered


def render_grid(player: Player,
                traps: list[Trap],
                treasure: Treasure,
                reveal: bool = False) -> str:
    """
    Build and return the full grid as a single string.

    Args:
        player:   the Player entity
        traps:    list of Trap entities
        treasure: the Treasure entity
        reveal:   if True, show trap positions (debug/game-over mode)
    """
    # Build a position → symbol lookup
    entity_map: dict[tuple, str] = {}

    for trap in traps:
        if trap.is_active:
            symbol = trap.symbol if reveal else HIDDEN_TRAP
        else:
            symbol = trap.symbol   # triggered traps always visible
        entity_map[trap.get_position()] = symbol

    entity_map[treasure.get_position()] = treasure.symbol
    entity_map[player.get_position()]   = player.symbol   # player drawn last (on top)

    # Render rows
    lines = [H_BORDER]
    for row in range(GRID_SIZE):
        cells = []
        for col in range(GRID_SIZE):
            cells.append(entity_map.get((col, row), EMPTY_CELL))
        lines.append("| " + " | ".join(cells) + " |")
        lines.append(H_BORDER)

    return "\n".join(lines)


def render_hud(player: Player, turn: int) -> str:
    """Return a one-line status bar shown above the grid."""
    return (
        f"  Turn {turn:>3}  │  Health: {player.health_bar()}  │  "
        f"Move: W↑ A← S↓ D→  │  Q = quit"
    )

"""
PERSON 5 – Game Manager
Responsibility: Initialise all entities, run the main game loop,
handle win/lose conditions, and orchestrate the other modules.

Run with:
    python person5_game.py
"""

import os
import random

GRID_SIZE  = 5
NUM_TRAPS  = 4


# ── Utility ──────────────────────────────────────────────────────────
def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def random_position(exclude: list[tuple]) -> tuple[int, int]:
    """Return a random (x, y) not already in `exclude`."""
    while True:
        pos = (random.randint(0, GRID_SIZE - 1),
               random.randint(0, GRID_SIZE - 1))
        if pos not in exclude:
            return pos


# ── Initialisation ───────────────────────────────────────────────────
def initialise_game() -> tuple[Player, list[Trap], Treasure]:
    taken = []

    # Player always starts top-left
    player = Player(x=0, y=0)
    taken.append(player.get_position())

    # Treasure placed bottom-right corner
    treasure = Treasure(x=GRID_SIZE - 1, y=GRID_SIZE - 1)
    taken.append(treasure.get_position())

    # Traps placed randomly in remaining cells
    traps = []
    for _ in range(NUM_TRAPS):
        tx, ty = random_position(exclude=taken)
        traps.append(Trap(x=tx, y=ty))
        taken.append((tx, ty))

    return player, traps, treasure


# ── Game Loop ────────────────────────────────────────────────────────
def run_game() -> None:
    player, traps, treasure = initialise_game()
    detector = CollisionDetector()
    turn     = 1
    message  = "🗺  Find the treasure (T). Watch out for hidden traps!"

    while True:
        clear_screen()

        # HUD + grid
        print()
        print(render_hud(player, turn))
        print()
        print(render_grid(player, traps, treasure))
        print()

        # Last-turn message
        if message:
            print(f"  {message}")
            print()

        # Input
        key = input("  Your move: ").strip().lower()
        print()

        if key == "q":
            print("  You fled the labyrinth. Goodbye!")
            break

        # Movement
        moved = player.move(key)
        if not moved:
            message = "🚧 Can't move there – that's a wall!"
            continue

        turn += 1

        # Collision detection
        result = detector.check(player, traps, treasure)
        message = result["message"]

        # Win condition
        if result["hit_treasure"]:
            clear_screen()
            print()
            print(render_grid(player, traps, treasure, reveal=True))
            print()
            print(f"  {message}")
            print(f"  Completed in {turn} turns.")
            print()
            break

        # Lose condition
        if not player.is_alive():
            clear_screen()
            print()
            print(render_grid(player, traps, treasure, reveal=True))
            print()
            print(f"  {message}")
            print()
            break


# ── Entry Point ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print()
    print("  ╔══════════════════════════════╗")
    print("  ║    M E M O R Y   L A B Y    ║")
    print("  ║       R I N T H  v1.0       ║")
    print("  ╚══════════════════════════════╝")
    print()
    input("  Press ENTER to begin...")
    run_game()
    input("  Press ENTER to exit.")

