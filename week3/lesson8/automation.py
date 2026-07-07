from pathlib import Path

class Config:
    source_path: Path
    destination_path: Path
    dry_run: bool = True

EXTENSION_MAP = {
    'Images' : ['.jpg', '.jpeg', '.png', '.svg'],
    'Videos' : ['.mp4'],
    'Documents' : ['.pdf', '.doc', '.docx'],
    'Audio' : ['.wav'],
    'Code' : ['.py', '.pyc', '.js'],
    'Archives' : ['.tar', '.tar.gz', '.tar.xz'],
}