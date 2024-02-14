import csv
with open('vacancy.csv','r',encoding='utf-8',newline='') as f: #создаем список из файла csv
    reader=csv.reader(f,delimiter=';')
    vacancy=list(reader)[1:]
def midsalary(a,b):
    '''
    Функция получает на вход две переменные

    переменная a - это название вакансии
    переменная b - это список в котором находятся вакансии

    Функция возвращает среднюю зарплату вакансии
    '''
    k=0 #Количество вакансий
    l=0 #Суммарная зарплата
    a=a.lower() #Переводим название вакансии в прописные буквы во избежание пропуска некоторых компаний
    for i in range(0,len(b)):
        if b[i][1].lower()==a:
            k+=1
            l+=int(b[i][0])
    midsa=int(l/k) #Ищем среднее значение зарплаты
    return midsa
vacancy=sorted(vacancy,key=lambda x:x[1],reverse=True) #Сортируем по вакансиям
for i in range(len(vacancy)): #Идем по списку
    k=midsalary(vacancy[i][1],vacancy) #Получаем среднее значение зарплаты
    k1=int((int(vacancy[i][0])/k)*100) #Получаем процент от средней зарплаты
    vacancy[i].append(str(k1)+'%') #Добавляем процент в список
with open('vacancy_procent.csv','w',encoding='utf-8',newline='') as f: #Создаем новый файл csv с процентом зарплат
    writer=csv.writer(f,delimiter=';')
    writer.writerow(['Salary','Work_Type','Company_Size','Role','Company','percent'])
    writer.writerows(vacancy)