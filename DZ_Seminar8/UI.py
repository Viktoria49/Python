import display
import fileio
import func


def menu(data):
    while True:
        answer = display.display_menu()
        if answer == 0:
            display.display_data(data)
        elif answer == 1:
            str_data = input("Please enter your data delimited by ';' : ")
            func.add_row(str_data, data)