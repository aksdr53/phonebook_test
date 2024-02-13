"""
Module to generate random data and write it to a text file.

This module generates random contact entries and writes them to a text file named 'phonebook.txt'.

Attributes:
    first_name (list): List of first names for random selection.
    family_name (list): List of family names for random selection.
    last_name (list): List of last names for random selection.
    organization (list): List of organization types for random selection.

Functions:
    random_numbers(): Generate a random phone number within a specific range.
    start(): Generate 100 random contact entries and write them to 'phonebook.txt'.
"""
import random
import json


pb = open('phonebook.txt', 'w')


first_name: list = ['Svetlana', 'Olga', 'Anton', 'Anna', 'Inna',
                    'Viktor', 'Vasilisa', 'Alex', 'Miron', 'Igor', 'Anna']
family_name: list = ['Kovalenko', 'Sidorenko', 'Mironenko',
                     'Galich', 'Shapiro', 'Duma', 'Duma', 'Shagal', 'Moroz']
last_name: list = ['Aleksandrovich', 'Borisovich', 'Olegovich', 'Timofeevich',
                   'Alekseevich',
                   'Petrovich', 'Kuzmich']
organization: list = [
    'OOO',
    'IP',
    'ZAO',
    'LLC'
]


def random_numbers() -> str:
    """
    Generate a random phone number within the range of 79000000000 to 80000000000.

    Returns:
        str: Random phone number as a string.
    """
    randomListPhone: int = random.randint(79000000000, 80000000000)
    return str(randomListPhone)


def start() -> None:
    """
    Generate 100 random contact entries and write them to 'phonebook.txt'.
    Each entry includes a family name, first name, last name, organization, work number, and personal number.
    """
    for i in range(100):
        entry = {
            'family_name': random.choice(family_name),
            'first_name': random.choice(first_name),
            'last_name': random.choice(last_name),
            'organization': random.choice(organization),
            'work_number': random_numbers(),
            'personal_number': random_numbers()
        }
        entry = json.dumps(entry)
        print(entry, file=pb)
    pb.close()


if __name__ == '__main__':
    start()