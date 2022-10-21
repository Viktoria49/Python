import random


def phone_numbers():
    phone_number = ['+' + str(random.randint(79000000000, 80000000000))]
    return ' '.join(phone_number)


def create_name():
    with open('Homework7//base_file//name.txt', 'r', encoding='UTF-8') as file:
        text = file.readlines()
        name = text[random.randint(0, 89)].replace('\n', ' ')
    return name


def create_surname():
    with open('Homework7//base_file//surname.txt', 'r', encoding='UTF-8') as file:
        text = file.readlines()
        surname = text[random.randint(0, 32)].replace('\n', ' ')
    return surname


def len_pnonebook():
    with open('Homework7//phonebook.csv', 'r', encoding='UTF-8') as file:
        phonebook_counter = len(file.readlines())
    return phonebook_counter
