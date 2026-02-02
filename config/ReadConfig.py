import json

def getConfig(configFile):
    with open(configFile, 'r') as f:
        data = json.load(f)
    return data