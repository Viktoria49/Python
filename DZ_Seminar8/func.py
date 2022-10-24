def add_row(str_data, data):
    row = str_data.split(";")
    data.append([row[0], row[1], row[2]])


def dell_str(str_to_del, data):
    for i in range(len(data)):
        if data[i][0] == str_to_del:
            del (data[i])
