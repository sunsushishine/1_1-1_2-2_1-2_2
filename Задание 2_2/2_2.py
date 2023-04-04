import csv

arr = {}
temp_name = 'Россия'
temp_max = 0
r=0
i=1

with open('opendata.csv', encoding='cp1251') as csvfile:
    credit_reader = csv.reader(csvfile, delimiter=',')
    for row in credit_reader:
        if row[0] == 'Количество заявок на потребительские кредиты':
            lst = row[2].split('-')
            if lst[0]=='2017':
                if temp_name == row[1]:
                    temp_max += int(row[3])
                else:
                    arr[temp_name]=temp_max
                    temp_max=0
                    temp_name = row[1]
                    temp_max += int(row[3])
              
for word, count in sorted(arr.items(), key=lambda item: item[1], reverse=True):
    print(f"{i} {word} -> {count}")
    i+=1
    r+=1
    if r ==10:
        break
print('регионом с максимальным количеством заявок на потребительские кредиты в 2017 г. является:',max(arr, key=arr.get))
