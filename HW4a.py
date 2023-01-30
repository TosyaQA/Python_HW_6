# Создайте список из случайных чисел. Найдите количество различных элементов в нем.
# Пример: 3, 7, 3, 4

array = input("Введите список через пробел: ").split()
unique_array = []

for x in array:
    if x not in unique_array:
        unique_array.append(x)

print(len(unique_array))