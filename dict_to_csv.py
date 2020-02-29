#Домашнее задание №3
#Работа csv
#* Создайте список словарей с ключами name, age и job
#* Запишите содержимое списка словарей в файл в формате csv

import csv

data_list=[
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

def main():
    with open('list.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for worker in data_list:
            writer.writerow(worker)
    pass

if __name__ == '__main__':
    main()