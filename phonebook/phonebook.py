import json

from constant import NEW_EDIT_PHRASE


class PhoneBook():

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def write_to_file(self, string: str) -> None:
        with open(self.filename, 'a') as pb:
            print(string, file=pb)
    
    def find(self, searched_entry: dict) -> list:
        result = []
        with open(self.filename, 'r') as pb:
            for entry in pb:
                entry = json.loads(entry)
                i = 0
                for key in searched_entry:
                    if (searched_entry[key] != entry[key]
                            and searched_entry[key] != ''):
                        break
                    i += 1
                if i == len(searched_entry):
                    result.append(json.dumps(entry))
        return result
    
    def get_all(self) -> list:
        with open(self.filename, 'r') as pb:
            return pb.readlines()
    
    def replace(self, entry: dict, replace: dict) -> None:
        entry = json.dumps(entry)
        replace = json.dumps(replace)
        lines = self.get_all()
        new_line = []
        for line in lines:
            line = line.strip()
            if line == entry:
                print(NEW_EDIT_PHRASE)
                new_line.append(replace)
            else:
                new_line.append(line)
        with open(self.filename, 'w') as pbw:
            for line in new_line:
                print(line, file=pbw)
