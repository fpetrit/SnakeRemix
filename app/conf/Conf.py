import json
from pathlib import Path

# OPEN AND LOAD THE CONFIGURATION FILE

cf_path = Path(__file__).parent.resolve() / "config.json"

conf_file = open(cf_path, 'r')

cf = json.loads(conf_file.read())


# ADDING THE ROOT DIRECTORY PATH TO THE LOADED CONFIGURATION

root_dir = Path(__file__).parents[2].resolve()
assets_dir = root_dir / "app" / "assets"

cf["App"]["root_dir"] = root_dir
cf["App"]["assets_dir"] = assets_dir


# CONSTANTS

KEYBINDS = cf["Keybinds"]
SNAKE_CF = cf["Snake"]
BG_CF = cf["Background"]

# Snake's directions
LEFT, RIGHT, UP, DOWN = [-1, 0], [1, 0], [0, -1], [0, 1]
