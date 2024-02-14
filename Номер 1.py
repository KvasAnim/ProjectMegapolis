import csv
with open('vacancy.csv','r',encoding='utf-8',newline='') as f: #создаем список из файла csv
    reader=csv.reader(f,delimiter=';')
    vacancy=list(reader)[1:]
vacancy.sort(reverse=True) #сортируем по убыванию
vacancy_new=[] #создаем новый список и добавляем три столбца:Название компании, Роль, Зарплата
for i in range(len(vacancy)):
    n=[vacancy[i][4], vacancy[i][3], vacancy[i][0]]
    vacancy_new.append(n)
with open('vacancy_new.csv','w',encoding='utf-8',newline='') as f: #Создаем новый файл csv
    writer=csv.writer(f,delimiter=';')
    writer.writerow(['company', 'role', 'Salary']) #Первой строчкой записываем заголовки
    writer.writerows(vacancy_new)
for i in range(0,3): #выводим первые 3 компании с наивышей зарплатой
    print(f'{vacancy_new[i][0]}-{vacancy_new[i][1]}-{vacancy_new[i][2]}')