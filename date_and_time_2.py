#Домашнее задание №1

#* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import datetime


def str_2_datetime(date_string):
    
    date_dt=datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

    return date_dt


if __name__ == '__main__':
    print(str_2_datetime('01/01/17 12:10:03.234567'))