# Задача 1
a = [1, 2, 3, 4, 5, 6]
for i in a:
    if i % 2 == 1:
        a.remove(i)
print(a)

for i in range(len(a)):
    a[i] = a[i] // 2
print(a)

# for i in a:
#     if i % 2 == 0:
#         print("Число четное", i, ': 2 = ', i / 2)

# Задача 3
a = int(input("Введи число a: "))
b = int(input("Введи число b: "))
my_list = []
new_list = []
for i in range(a, b + 1):
    if i % 3 == 0:
        my_list.append(i)
result = sum(my_list)
print(result / len(my_list) )