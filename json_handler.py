import json

FILEPATH = "light.json"

class config_handler:

    def __init__(self) -> None:
        self.lights = self.load_json()

    def load_json(self):
        with open(FILEPATH, "r") as file:
            data = json.load(file)
        return data

    def get_lights_all(self):
        return self.lights["lights"]

    def get_light_by_id(self, id):
        try:
            return self.lights["lights"][id]
        except Exception as r:
            print(r)
            return ""

    def set_state_light(self, id, data):
        for key in data.keys():
            self.lights["lights"][id][key] = data[key]

    def remove_light(self, id):
        self.lights["lights"][id] = ""



    def get_groups_all(self):
        return self.lights["groups"]

    def get_group_by_id(self, id):
        try:
            return self.lights["groups"][id]
        except Exception as r:
            print(r)
            return ""

    def set_state_group(self, id, data):
        for key in data.keys():
            self.lights["groups"][id][key] = data[key]

    def add_to_group(self, id, data):
        self.lights["groups"][id]["lights"].append(data["lights"])

    def remove_group(self, id):
        self.lights["groups"][id] = ""

