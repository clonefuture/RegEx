from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# Приводим ФИО к одному виду во всех записях

for id_1, st in enumerate(contacts_list[1:], 1):
    new_lst = []
    for id_2, item in enumerate(st[:3]):
        lst = (re.split(' ', item))
        new_lst = new_lst + lst
        contacts_list[id_1][id_2] = new_lst[id_2]

# Объединяем данные по каждому сотруднику

co_st = []
NN = contacts_list
for i in range(len(NN) - 1):
    for j in range(i + 1, len(NN)):
        if NN[i][0] == NN[j][0] and NN[i][1] == NN[j][1]:
            for sn in range(len(NN[i])):
                if len(contacts_list[i][sn]) == 0:
                    contacts_list[i][sn] = contacts_list[j][sn]
            co_st += [j]

# Удаляем дублирующие записи в справочнике

for i in reversed(co_st):
    contacts_list.pop(i)

# Редактируем телефонные номера с помощью регулярных выражений

for i in range(1, len(contacts_list)):
    if 'доб' not in contacts_list[i][5]:
        result = re.sub(r'(\+7|8)\s*\(?(\d{3})\)?[\-\s]?(\d{3})\s*[-\s]?(\d{2})[-\s]?(\d+)', r'+7(\2)\3-\4-\5',
                        contacts_list[i][5])
        contacts_list[i][5] = result
    else:
        result = re.sub(r'(\+7|8)\s*\(?(\d{3})\)?[\-\s]?(\d{3})\s*[-\s]?(\d{2})[-\s]?(\d+)\s*\(?\w*\.?\s?(\d*)\)?',
                        r'+7(\2)\3-\4-\5 доб.\6',
                        contacts_list[i][5])
        contacts_list[i][5] = result

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)
