import random 
while True:
    try:
        x=int(input("Введите количество столбцов -> "))
        y=int(input("Введите количество строк -> "))
        z=int(input("Начало диапозона -> "))
        c=int(input("Конец диапозона -> "))
        break
    except ValueError:
        print ("Надо ввести число")

arr = []
temp = []
for j in range(y):
    for i in range(x):
        temp.append(random.randint(z,c))
    arr.append(temp)
    temp=[]
for z in range(y):
    print(arr[z])

