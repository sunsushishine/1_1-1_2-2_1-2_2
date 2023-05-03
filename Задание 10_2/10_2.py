def func(num):
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp !=  0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False
    
for i in range(200):
    pal = func(i)
    if pal:
        print(pal)
