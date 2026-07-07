import random

print("=== WELCOME TO THE FIFA WORLD CUP 2026 MANAGER ===\n")

team_name = input("Enter your team's name: ")
morale = 70
strength = 70
injuries = 0
points = 0
stage = "Pre-Tournament"

print(f"\n{team_name} squad initialized. Morale: {morale}, Strength: {strength}\n")

# ---------- PRE-TOURNAMENT PREPARATION ----------
day = 1
while day <= 5:
    print(f"--- Pre-Tournament Day {day} ---")
    print("1. Training  2. Friendly Match  3. Rest/Recovery")
    choice = input("Choose an activity: ")

    if choice == "1":
        strength += 5
        morale -= 2
        print("Training complete. Strength +5, Morale -2")
    elif choice == "2":
        result = random.choice(["win", "draw", "loss"])
        if result == "win":
            morale += 5
            print("Friendly won! Morale +5")
        elif result == "draw":
            print("Friendly drawn. No change.")
        else:
            morale -= 5
            injuries += 1
            print("Friendly lost and a player got injured. Morale -5, Injuries +1")
    elif choice == "3":
        morale += 5
        print("Recovery day. Morale +5")
    else:
        # invalid input, skip this day without penalty
        print("Invalid choice, skipping this day.")
        day += 1
        continue

    if injuries >= 3:
        print("\nToo many injuries before the tournament even starts!")
        print("Team withdraws from World Cup 2026.")
        break

    day += 1

else:
    # while-else: runs only if loop wasn't broken
    print(f"\nPre-tournament complete! Final stats -> Morale: {morale}, Strength: {strength}, Injuries: {injuries}\n")
    stage = "Group Stage"

    # ---------- GROUP STAGE (3 MATCHES) ----------
    match_num = 1
    while match_num <= 3:
        print(f"--- Group Match {match_num} ---")

        if injuries >= 3:
            print("Squad too depleted to continue.")
            break

        # pass placeholder for future feature (e.g., choosing tactics)
        pass

        team_power = strength + morale - (injuries * 10)
        opponent_power = random.randint(60, 100)

        print(f"Your team power: {team_power} | Opponent power: {opponent_power}")

        if team_power > opponent_power:
            print("Result: WIN!")
            points += 3
            morale += 5
        elif team_power == opponent_power:
            print("Result: DRAW.")
            points += 1
        else:
            print("Result: LOSS.")
            morale -= 5
            if random.random() < 0.3:
                injuries += 1
                print("A key player got injured during the match!")

        match_num += 1

    print(f"\nGroup stage complete. Points: {points}, Morale: {morale}, Injuries: {injuries}\n")

    if points < 4:
        print(f"{team_name} did not qualify for the knockout stage. Tournament over.")
    else:
        print(f"{team_name} qualifies for the Knockout Stage!\n")

        # ---------- KNOCKOUT STAGES ----------
        knockout_stages = ["Round of 16", "Quarter-Final", "Semi-Final", "Final"]
        k = 0
        while k < len(knockout_stages):
            current_stage = knockout_stages[k]
            print(f"--- {current_stage} ---")

            if injuries >= 5:
                print("Squad decimated by injuries. Cannot continue.")
                break

            team_power = strength + morale - (injuries * 10)
            opponent_power = random.randint(70, 110)

            print(f"Your team power: {team_power} | Opponent power: {opponent_power}")

            if team_power > opponent_power:
                print(f"WIN! {team_name} advances past {current_stage}.\n")
                morale += 5

                if current_stage == "Final":
                    print(f"*** CONGRATULATIONS! {team_name} WINS THE FIFA WORLD CUP 2026! ***")
                    break  # tournament won, exit loop

                k += 1
            else:
                print(f"LOSS! {team_name} is eliminated at the {current_stage} stage.")
                break  # tournament lost, exit loop

print("\n=== SIMULATION ENDED ===")