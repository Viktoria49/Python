message = '''Что делаем?
0 - Просмотр
1 - Добавить запись
2 - Удалить запись под номером N
3 - Записать в файл
4 - Выход\n'''

def display_data(data):
    for line in data:
        print(line)


def display_menu():
    answer = int(input(message))
    return answer
