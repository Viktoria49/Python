import random
from datetime import date
import func


def create_phonebook():

    global id
    global name
    global surname
    global birthday
    global phone

    id = []
    name = []
    surname = []
    birthday = []
    phone = []

    n = int(input('Введите размер справочника '))
    print('id  Имя Фамилия День_рождения Телефон')
    for i in range(n):

        result = ' '
        id.append(i)
        name.append(func.create_name())
        surname.append(func.create_surname())
        birthday.append(date.today().replace(day=random.randint(
            1, 28), month=random.randint(1, 12), year=random.randint(1960, 2022)))
        phone = func.phone_numbers()
        result = str(id[i])+" "+str(name[i])+" "+str(surname[i]) + " " + \
            str(birthday[i]) + "  " + phone
        print(result)


def save_data():

    with open('Homework7//phonebook.csv', 'w', encoding='UTF-8') as file:
        for i in id:
            file.writelines(str(id[i])+" "+name[i]+" "+surname[i] +
                            " "+str(birthday[i])+" " + str(phone[i]) + "\n")


def add_record(name1, surname1, date, phone):
    global phonebook_counter
    phonebook_counter = func.len_pnonebook()
    result = [str(phonebook_counter), name1, surname1,
              date,  phone.replace(' ', ': ')]
    with open('Homework7//phonebook.csv', 'a', encoding='UTF-8') as file:
        file.write(','.join(result) + '\n')


def change_record(record_id, field, new_value):
    with open('Homework7//phonebook.csv', 'r', encoding='UTF-8') as file:
        file_lst = file.readlines()
    with open('Homework7//phonebook.csv', 'w', encoding='UTF-8') as file:
        for i in range(len(file_lst)):
            if i == record_id - 1:
                comma_places = [j for j in range(
                    len(file_lst[i])) if file_lst[i].startswith(',', j)]
                start = comma_places[field-1]
                try:
                    finish = comma_places[field]
                except:
                    finish = len(file_lst)-1
                if field != 5:
                    file_lst[i] = file_lst[i][:start+1] + \
                        new_value + file_lst[i][finish:]
                else:
                    file_lst[i] = file_lst[i][:start+1] + \
                        new_value.replace(' ', '; ') + \
                        file_lst[i][finish:]+'\n'
                file.write(file_lst[i])
            else:
                file.write(file_lst[i])


def delete_record(id):
    with open('Homework7//phonebook.csv', 'r', encoding='UTF-8') as file:
        file_lst = file.readlines()
    with open('Homework7//phonebook.csv', 'w', encoding='UTF-8') as file:
        for i in range(len(file_lst)):
            if i == id - 1:
                continue
            else:
                file.write(file_lst[i])


def delete_all():
    with open('Homework7//phonebook.csv', 'w', encoding='UTF-8') as file:
        file.write('')
