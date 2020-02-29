#Домашнее задание №2
#Работа с файлами
#* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
#* Подсчитайте количество слов в тексте



def main():
    with open('referat.txt', 'r', encoding='utf-8') as text_task:
        content=text_task.read()
        content=content.replace('\n', ' ')
        words=content.split()
        print(content)
        print(len(words))
            
    pass

if __name__ == "__main__":
    main()