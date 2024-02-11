import json
from os import system, name  

from constant import (START_PHRASE,
                      ADD_PHRASE,
                      FIND_PHRASE,
                      TABEL_HEAD,
                      PAGINATION_PHRASE,
                      EDIT_PHRASE)

def clear():
    if name == 'nt':  
        _ = system('cls')
    else:
        _ = system('clear')


def whrite_to_file(string):
    with open('phonebook.txt', 'a') as pb:
        print(string, file=pb)


def find(f_entry):
    result = []
    with open('phonebook.txt', 'r') as pb:
        for entry in pb:
            entry = json.loads(entry)
            i = 0
            for key in f_entry:
                if f_entry[key] != entry[key]:
                    break
                i += 1
            if i == len(f_entry):
                result.append(entry)
    return result


def entry_input():
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


def add_entry():
    print(ADD_PHRASE)
    entry = entry_input()
    entry = json.dumps(entry)
    whrite_to_file(entry)
    print('Запись введена')
    start()


def find_entry():
    print(FIND_PHRASE)
    entry = entry_input()
    f_entry = {}
    for key in entry:
        if entry[key] != '':
            f_entry[key] = entry[key]
    if not f_entry:
        print('Данныене не были введены')
        return start()
    result = find(f_entry)
    if result:
        entry_number = 1
        print(TABEL_HEAD)
        print('-' * 144 )
        for entry in result:
            print(str(entry_number).center(5), end='')
            for key in entry:
                print('|', f'{entry[key]}'.center(20), '|',  end='')
            print()
            entry_number += 1
        return start()
    clear()
    print('Записей соотвествующих вашему запросу не найдено')
    start()




def show_entrys():
    with open('phonebook.txt', 'r') as pb:
        print(TABEL_HEAD)
        print('-' * 144 )
        i = 1
        entry_number = 1
        for entry in pb:
            print(str(entry_number).center(5), end='')
            entry = json.loads(entry)
            for key in entry:
                print('|', f'{entry[key]}'.center(20), '|',  end='')
            print()
            i += 1
            entry_number += 1
            if i == 20:
                print(PAGINATION_PHRASE)
                command = str(input()).strip()
                if command != 'next':
                    return start()
                print(TABEL_HEAD)
                print('-' * 144 )
    start()


def edit_entry():
    print(EDIT_PHRASE)
    entry = entry_input()
    if len(entry) < 6:
        print('Заполнены не все поля')
        start()
    result = find(entry)
    


def exit():
    print('До свидания')


COMMAND_DICT = {
    'add': add_entry,
    'find': find_entry,
    'show': show_entrys,
    'edit': edit_entry,
    'exit': exit
}


def start():
    print(START_PHRASE)
    command = str(input()).strip()
    while command not in COMMAND_DICT: 
        print(
            'Неверная команда\n'
            'Введите команду'
        )
        command = str(input()).strip()
    COMMAND_DICT[command]()



if __name__ == '__main__':
    start()