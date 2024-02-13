"""
Module starts the phonebook app
"""
from session import Sessiion
from phonebook import PhoneBook

phonebook = PhoneBook('phonebook.txt')
session = Sessiion(phonebook)
session.main_menu()