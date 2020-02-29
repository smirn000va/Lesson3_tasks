#Домашнее задание №2

#* Напечатайте в консоль даты: вчера, сегодня, месяц назад

from datetime import datetime, timedelta
import calendar

def print_days():

    dt_now=datetime.now()

    delta_yesterday=timedelta(days=1)
    dt_yesterday=dt_now-delta_yesterday

    days_in_month=calendar.monthrange(dt_now.year, dt_now.month)[1]
    dt_month_ago=dt_now-timedelta(days=days_in_month)
    
    dt_now.strftime('%Y.%m.%d %H:%M')
    dt_yesterday.strftime('%Y.%m.%d %H:%M')
    dt_month_ago.strftime('%Y.%m.%d %H:%M')

    print(dt_now)
    print(dt_yesterday)
    print(dt_month_ago)


if __name__ == "__main__":
    print_days()
    