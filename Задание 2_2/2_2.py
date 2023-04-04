import csv as file

list={}
temp_name='Россия'
temp_max=0
str=0
i=1

print('Первые 10 регионов')

with open('opendata.csv') as csvfile:
    credit_reader=file.reader(csvfile, delimiter=',')
    for row in credit_reader:
        if row[0]=='Количество заявок на потребительские кредиты':
            lst = row[2].split('-')
            if lst[0]=='2017':
                if temp_name==row[1]:
                    temp_max+=int(row[3])
                else:
                    list[temp_name]=temp_max
                    temp_max=0
                    temp_name=row[1]
                    temp_max+=int(row[3])

for word, count in sorted(list.items(), key=lambda item: item[1], reverse=True):
    print(f"{i} {word} -> {count}")
    i+=1
    str+=1
    if str==10:
        break

print('Регионом с максимальным количеством заявок на потребительские кредиты в 2017 году является:', max(list, key=list.get))
