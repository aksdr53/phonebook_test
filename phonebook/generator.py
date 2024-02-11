import random
import json


pb = open('phonebook.txt', 'w')


first_name = ['Svetlana', 'Olga', 'Anton', 'Anna', 'Inna',
              'Viktor', 'Vasilisa', 'Alex', 'Miron', 'Igor', 'Anna']
family_name = ['Kovalenko', 'Sidorenko', 'Mironenko',
               'Galich', 'Shapiro', 'Duma', 'Duma', 'Shagal', 'Moroz']
last_name = ['Aleksandrovich', 'Borisovich', 'Olegovich', 'Timofeevich',
             'Alekseevich',
             'Petrovich', 'Kuzmich']
organization = [
    'OOO',
    'IP',
    'ZAO',
    'LLC'
]


def random_numbers():
    randomListPhone = random.randint(79000000000, 80000000000)
    return str(randomListPhone)


def start():
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