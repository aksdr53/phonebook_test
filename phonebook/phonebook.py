import json
from os import system, name
import sys

from constant import (START_PHRASE,
                      ADD_PHRASE,
                      FIND_PHRASE,
                      TABEL_HEAD,
                      PAGINATION_PHRASE,
                      EDIT_PHRASE,
                      NEW_EDIT_PHRASE)


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


class Sessiion():

    def __init__(self, phonebook: PhoneBook) -> None:
        self.phonebook = phonebook

    def get_command(self) -> None:
        COMMAND_DICT = {
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

    def main_menu(self):
        while True:
            print(START_PHRASE)
            self.get_command()

    def entry_input(self):
        entry = {
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
        if not table:
            table = self.phonebook.get_all()
        print(TABEL_HEAD)
        print('-' * 144 )
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
                print('-' * 144 )

    def add_entry(self) -> None:
        print(ADD_PHRASE)
        entry = self.entry_input()
        entry = json.dumps(entry)
        self.phonebook.write_to_file(entry)
        print('Запись введена')
        self.main_menu()

    def check_fields(self, entry: dict) -> bool:
        f_entry = {}
        for key in entry:
            if entry[key] != '':
                f_entry[key] = entry[key]
        if not f_entry:
            print('Данныене не были введены')
            return False
        return True

    def find_entry(self) -> None:
        print(FIND_PHRASE)
        entry = self.entry_input()
        if not self.check_fields(entry):
            return
        result = self.phonebook.find(entry)
        if result:
            self.print_table(result)
        else:
            self.clear()
            print('Записей соотвествующих вашему запросу не найдено')

    def edit_entry(self) -> None:
        print(EDIT_PHRASE)
        entry = self.entry_input()
        if len(entry) < 6:
            print('Заполнены не все поля')
            return
        result = self.phonebook.find(entry)
        if len(result) != 1:
            print('Запись не найдена')
            return
        replace = self.entry_input()
        self.phonebook.replace(entry, replace)

    def exit(self) -> None:
        sys.exit()

    def clear(self) -> None:
        if name == 'nt':  
            _ = system('cls')
        else:
            _ = system('clear')


if __name__ == '__main__':
    phonebook = PhoneBook('phonebook.txt')
    session = Sessiion(phonebook)
    session.main_menu()