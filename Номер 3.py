import csv
with open('vacancy.csv','r',encoding='utf-8',newline='') as f: #создаем список из файла csv
    reader=csv.reader(f,delimiter=';')
    vacancy=list(reader)[1:]
co_name=input('Название компании:') #Переменная для ввода с клавиатуры названия компании
while co_name!='None': #Цикл пока не введено значение None
    k=0 #Переключатель если комания нашлась
    for i in range(0,len(vacancy)): #Выводим найденные компании
        if vacancy[i][4]==co_name:
            print(f'В {vacancy[i][4]} найдена вакансия: {vacancy[i][3]}. З/п составит: {vacancy[i][0]}')
            k=1 #Меняем переключатель на 1
    if k==0: #Если переключатель не был изменен, то выводим сообщение
        print('К сожалению, ничего не удалось найти')
    co_name=input('Название компании:') #Заново запрашиваем ввод с клавиатуры названия компании