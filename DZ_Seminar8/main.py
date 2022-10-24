# Закрепить знания по созданию модульных приложений. Создать прототип интерактивной базы данных..


import fileio
import UI

data = fileio.read_data("data.csv")
UI.menu(data)
