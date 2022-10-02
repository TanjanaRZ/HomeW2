# 5. Реализуйте алгоритм перемешивания списка.

import random

a = int(input("Введите число: "))
lst = [-a + i for i in range(a * 2 + 1)]
rez = []
print(lst)
for i in range(len(lst)):
    ind = random.randint(0, len(lst) - 1)
    rez.append(lst.pop(ind))

print(rez)