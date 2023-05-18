import json

__conf_file = open("config.json", 'r')

cf = json.loads(__conf_file.read())