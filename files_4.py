#Домашнее задание №2
#Работа с файлами
#* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
#* Подсчитайте количество слов в тексте
#* Замените точки в тексте на восклицательные знаки
#* Сохраните результат в файл referat2.txt



def main():

    with open('referat.txt', 'r', encoding='utf-8') as text_task:
        content=text_task.read()  
        content=content.replace('\n', ' ')
        content=content.replace('.', '!')
        print(content)
        
    with open('referat2.txt', 'w', encoding='utf-8') as text_task_2:
        text_task_2.write(content)

    pass

if __name__ == '__main__':
    main()