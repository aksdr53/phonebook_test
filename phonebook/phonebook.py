"""
PhoneBook Class

A class for managing a phonebook stored in a text file.

Attributes:
    filename (str): The name of the text file used to store the phonebook entries.

Methods:
    __init__(self, filename: str) -> None:
        Initializes the PhoneBook object with the specified filename.

    write_to_file(self, string: str) -> None:
        Appends the provided string to the phonebook file.

    find(self, searched_entry: dict) -> list:
        Searches for entries in the phonebook that match the specified criteria.

    get_all(self) -> list:
        Retrieves all entries from the phonebook file.

    replace(self, entry: dict, replace: dict) -> None:
        Replaces an existing entry in the phonebook with a new one.

"""
import json


class PhoneBook():

    def __init__(self, filename: str) -> None:
        """
        Initializes the PhoneBook object with the specified filename.

        Parameters:
            filename (str): The name of the text file used to store the phonebook entries.
        """
        self.filename = filename

    def write_to_file(self, string: str) -> None:
        """
        Appends the provided string to the phonebook file.

        Parameters:
            string (str): The string to be appended to the phonebook file.
        """
        with open(self.filename, 'a') as pb:
            print(string, file=pb)
    
    def find(self, searched_entry: dict) -> list:
        """
        Searches for entries in the phonebook that match the specified criteria.

        Parameters:
            searched_entry (dict): Dictionary containing the criteria for searching.

        Returns:
            list: List of matching entries in JSON format.
        """
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
        """
        Retrieves all entries from the phonebook file.

        Returns:
            list: List of all entries in the phonebook file.
        """
        with open(self.filename, 'r') as pb:
            return pb.readlines()
    
    def replace(self, entry: dict, replace: dict) -> None:
        """
        Replaces an existing entry in the phonebook with a new one.

        Parameters:
            entry (dict): The entry to be replaced.
            replace (dict): The new entry to replace the existing one.
        """
        entry = json.dumps(entry)
        replace = json.dumps(replace)
        lines = self.get_all()
        new_line = []
        for line in lines:
            line = line.strip()
            if line == entry:
                new_line.append(replace)
            else:
                new_line.append(line)
        with open(self.filename, 'w') as pbw:
            for line in new_line:
                print(line, file=pbw)
