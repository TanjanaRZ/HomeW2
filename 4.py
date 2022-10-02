# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле 
#  file.txt в одной строке одно число.

a = int(input("Число: "))
lst = [-a + i for i in range(a * 2 + 1)]
print(lst)
f = open("file.txt")
prz = 1
for i in f.readlines():
    if int(i) < len(lst):
        prz *= lst[int(i)]
print(prz)
