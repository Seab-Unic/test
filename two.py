import random
n = float(input("Введите число "))
a = random.randint(1,10)
b = random.randint(10,21)
if a <= n <= b:
    print("принадлежит")
else:
    print("не принадлежит")
