import csv
with open('vacancy.csv','r',encoding='utf-8',newline='') as f: #создаем список из файла csv
    reader=csv.reader(f,delimiter=';')
    vacancy=list(reader)[1:]
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.+&()'- АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫБЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890"
alp={}
for x in range(len(a)):
    alp[a[x]]=x+1
def HashGen(a,alp):
    p=141
    m=10**9+7
    hash_val=0
    ps=1
    for c in a:
        hash_val=(hash_val+alp[c]*ps)%m
        ps=(ps*p)%m
    return int(hash_val)
for i in range(len(vacancy)):
    k=(HashGen(vacancy[i][4],alp))
    vacancy[i][4]=k
vacancy_hash={}
vacancy.sort(key=lambda x:x[4])
k=0
for i in range(len(vacancy)):
    if k==vacancy[i][4]:
        vacancy_hash[k].append([vacancy[i][0],vacancy[i][1],vacancy[i][2]])
    else:
        k=vacancy[i][4]
        vacancy_hash[k]=[]
        vacancy_hash[k].append([vacancy[i][0],vacancy[i][1],vacancy[i][2]])
l=input('Введите название компании: ')
l=HashGen(l,alp)
print(f'{vacancy_hash[l]},{vacancy_hash[l]},{vacancy_hash[l]}')