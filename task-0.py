import random
a = [random.randint(-100, 100)for i in range(30)]
maxnum = max(a)
a.index(maxnum)
print(a)
print("Макс. елем: " + str(maxnum))
print("Порядковий номер числа: " + str(a.index(maxnum)+1))
print("пари чисел, що стоять рядом: ")
for i in range(29):
    if a[i]<0 and a[i+1]<0:
        print("Числа: " + str(a[i]) + " та " + str(a[i+1]))
