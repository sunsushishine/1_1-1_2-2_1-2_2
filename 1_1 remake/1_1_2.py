import random

arr = []
temp = []

while True:
    try:
        cT=int(input("Введите кол-во столбцов -> "))
        cS=int(input("Введите кол-во строк -> "))
        start=int(input("Начало диапозона -> "))
        end=int(input("Конец диапозона -> "))
        break
    except ValueError:
        print("Требуется число!")

for x in range(cS):
    for y in range(cT):
        temp.append(random.randint(start, end))
    arr.append(temp)
    temp=[]
for z in range(cS):
    print(arr[start])