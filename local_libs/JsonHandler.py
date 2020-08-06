import json


class JsonHandler:

    def __init__(self, data: dict = {}, file: bool = False, patch: str = "./"):
        self.file = file
        self.data = data
        self.patch = patch

    def read(self) -> dict:
        if self.file:
            with open(self.patch, 'r') as file:
                json_data = json.load(file)
        else:
            json_data = self.data
        return json_data

    def save(self, to_json: dict) -> dict:
        if self.file:
            with open(self.patch, 'w') as file:
                json.dump(to_json, file, indent=4)
        return to_json

    def update(self, what: dict, parse_to: str = "") -> dict:
        obj = self.read()
        to_exec = f"""data = obj{parse_to}; a= data.update(what) if type(data) == dict else data.append(what)"""
        exec(to_exec)
        return self.save(obj)

    def delete(self, what: any, parse_to: str = "") -> dict:
        obj = self.read()
        exec("obj" + parse_to + ".pop(what)")
        return self.save(obj)

    def replaceByName(self, param: str, what: any, parse_to: str = "") -> dict:
        obj = self.read()
        exec("obj" + parse_to + "['" + param + "'] = what")
        return self.save(obj)
