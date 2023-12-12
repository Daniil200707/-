import json

class Level:

    def __init__(self):
        with open("resource/JSON/level.json", "r") as file:
            self.json_level = json.load(file)

    def get_level(self):
        return self.json_level["level"]
