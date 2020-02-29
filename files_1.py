#Домашнее задание №2
#Работа с файлами
#* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
#* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки



def main():
    with open('referat.txt', 'r', encoding='utf-8') as text_task:
        for line in text_task:
            Len_text=len(line)
            print(line)
            print(Len_text)
            
    pass

if __name__ == "__main__":
    main()