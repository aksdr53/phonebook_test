"""
Session Class

A class representing a session for managing a phonebook through a command-line interface.

Attributes:
    phonebook (PhoneBook): An instance of the PhoneBook class to manage phonebook entries.

Methods:
    __init__(self, phonebook: PhoneBook) -> None:
        Initializes the Session object with the provided PhoneBook instance.

    get_command(self) -> None:
        Reads user input for commands and executes corresponding methods.

    main_menu(self) -> None:
        Displays the main menu and continuously prompts the user for commands.

    entry_input(self) -> dict:
        Takes user input for a new phonebook entry and returns it as a dictionary.

    print_table(self, table: list = []) -> None:
        Prints the phonebook entries in a tabular format with pagination.

    add_entry(self) -> None:
        Prompts the user for input and adds a new entry to the phonebook.

    check_fields(self, entry: dict) -> bool:
        Checks if the required fields in a phonebook entry are filled.

    find_entry(self) -> None:
        Prompts the user for search criteria and displays matching entries.

    edit_entry(self) -> None:
        Prompts the user for an entry to edit and replaces it with a new entry.

    exit(self) -> None:
        Exits the program.

    clear(self) -> None:
        Clears the console screen.

"""
from os import system, name
import sys
import json

from phonebook import PhoneBook
from constant import (START_PHRASE,
                       ADD_PHRASE,
                       FIND_PHRASE,
                       TABEL_HEAD,
                       PAGINATION_PHRASE,
                       EDIT_PHRASE,
                       NEW_EDIT_PHRASE)


class Sessiion():

    def __init__(self, phonebook: PhoneBook) -> None:
        """
        Initializes the Session object with the provided PhoneBook instance.

        Parameters:
            phonebook (PhoneBook): An instance of the PhoneBook class to manage phonebook entries.
        """
        self.phonebook = phonebook

    def get_command(self) -> None:
        """
        Reads user input for commands and executes corresponding methods.
        """
        COMMAND_DICT: dict = {
            'add': self.add_entry,
            'find': self.find_entry,
            'show': self.print_table,
            'edit': self.edit_entry,
            'exit': self.exit
        }
        command = str(input()).strip()
        while command not in COMMAND_DICT: 
            print(
                'Неверная команда\n'
                'Введите команду'
            )
            command = str(input()).strip()
        COMMAND_DICT[command]()

    def main_menu(self) -> None:
        """
        Displays the main menu and continuously prompts the user for commands.
        """
        while True:
            print(START_PHRASE)
            self.get_command()

    def entry_input(self) -> dict:
        """
        Takes user input for a new phonebook entry and returns it as a dictionary.

        Returns:
            dict: Dictionary representing a phonebook entry.
        """
        entry: dict = {
            'family_name': '',
            'first_name': '',
            'last_name': '',
            'organization': '',
            'work_number': '',
            'personal_number': ''
        }
        for key in entry:
            entry[key] = input(f'Введите {key} :').strip()
        return entry

    def print_table(self, table: list = []) -> None:
        """
        Prints the phonebook entries in a tabular format with pagination.

        Parameters:
            table (list): List of phonebook entries to display.
        """
        if not table:
            table: list = self.phonebook.get_all()
        print(TABEL_HEAD)
        print('-' * 144)
        i = 1
        entry_number = 1
        for entry in table:
            print(str(entry_number).center(5), end='')
            entry = json.loads(entry)
            for key in entry:
                print('|', f'{entry[key]}'.center(20), '|',  end='')
            print()
            i += 1
            entry_number += 1
            if i % 20 == 0:
                print(PAGINATION_PHRASE)
                command = str(input()).strip()
                if command != 'next':
                    return
                print(TABEL_HEAD)
                print('-' * 144)

    def add_entry(self) -> None:
        """
        Prompts the user for input and adds a new entry to the phonebook.
        """
        print(ADD_PHRASE)
        entry: dict = self.entry_input()
        entry = json.dumps(entry)
        self.phonebook.write_to_file(entry)
        print('Запись введена')
        self.main_menu()

    def check_fields(self, entry: dict) -> bool:
        """
        Checks if the required fields in a phonebook entry are filled.

        Parameters:
            entry (dict): The phonebook entry to check.

        Returns:
            bool: True if all required fields are filled, False otherwise.
        """
        f_entry = {}
        for key in entry:
            if entry[key] != '':
                f_entry[key] = entry[key]
        if not f_entry:
            print('Данныене не были введены')
            return False
        return True

    def find_entry(self) -> None:
        """
        Prompts the user for search criteria and displays matching entries.
        """
        print(FIND_PHRASE)
        entry: dict = self.entry_input()
        if not self.check_fields(entry):
            return
        result = self.phonebook.find(entry)
        if result:
            self.print_table(result)
        else:
            self.clear()
            print('Записей соотвествующих вашему запросу не найдено')

    def edit_entry(self) -> None:
        """
        Prompts the user for an entry to edit and replaces it with a new entry.
        """
        print(EDIT_PHRASE)
        entry: dict = self.entry_input()
        if len(entry) < 6:
            print('Заполнены не все поля')
            return
        result: list = self.phonebook.find(entry)
        if len(result) != 1:
            print('Запись не найдена')
            return
        self.clear()
        print(NEW_EDIT_PHRASE)
        replace: dict = self.entry_input()
        self.phonebook.replace(entry, replace)

    def exit(self) -> None:
        """
        Exits the program.
        """
        sys.exit()

    def clear(self) -> None:
        """
        Clears the console screen.
        """
        if name == 'nt':  
            _ = system('cls')
        else:
            _ = system('clear')