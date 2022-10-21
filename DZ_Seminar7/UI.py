import controller as c


def menu():
    while True:
        print('\nВыберете пункт меню:\n'
              '\n1 - Сгенерировать справочник.\n'
              '2 - Сохранить справочник в файл.\n'
              '3 - Добавить запись в файл.\n'
              '4 - Изменить запись в файле.\n'
              '5 - Удалить строку.\n'
              '6 - Очистить справочник.\n'
              '7 - Выход.\n')
        number_menu = input('Введите номер пункта меню: ')

        if number_menu.isdigit() and int(number_menu) in range(1, 8):

            if int(number_menu) == 1:
                c.create_phonebook()

            elif int(number_menu) == 2:
                c.save_data()

            elif int(number_menu) == 3:
                name = input("Введите имя: ")
                surname = input("Введите фамилию: ")
                date = input("Введите день рождения: ")
                phone = input("Введите телефон: ")
                c.add_record(name, surname, date, phone)

            elif int(number_menu) == 4:
                record_id = int(input("Введите номер строки для изменения: "))
                field = int(
                    input("Введите номер поля для изменения от 1 до 4: "))
                new_value = input("Введите новое значение: ")
                c.change_record(record_id, field, new_value)

            elif int(number_menu) == 5:
                record_id = int(input("Введите номер строки для удаления: "))
                c.delete_record(record_id)

            elif int(number_menu) == 6:
                c.delete_all()

            elif int(number_menu) == 7:
                print('До свидания!')
                break

        else:
            print(
                '\nТакого пункта меню нет.\n'
                'Введите цифру, соответствующую пункту меню.')
