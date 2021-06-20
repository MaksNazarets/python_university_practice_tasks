import random

my_list = []

print("The list:")
for i in range(30):
    my_list.append(random.randint(-100, 100))

print(my_list)

#Знаходження найбільшого числа та його порядкового номера
max_number = -100
max_indeces = []

    #Записуємо індекс найбільшого числа.
    #Якщо їх кілька, зберігаємо до списку індекс кожного
for i, item in enumerate(my_list):
    if item > max_number:
        max_number = item
        max_indeces.clear()
        max_indeces.append(i)
    elif item == max_number:
        max_indeces.append(i)

    #Красивий вивід на екран)
print(f"\nThe largest number: {max_number} (", end="")
if len(max_indeces) == 1:
    print("element №", end="")
    print(max_indeces[0] + 1, end="")
else:
    print(f"elements №{max_indeces[0] + 1}", end="")
    for i in max_indeces:
        if i != max_indeces[0]:
            print(f', №{i + 1}', end="")
print (")")

#Знаходження пар від'ємних чисел, що стоять поруч
print("\nThe pairs of negative numbers:")
for i in range(len(my_list)):
    if i >= 1 and my_list[i] < 0 and my_list[i - 1] < 0:
        print(f'{my_list[i - 1]}, {my_list[i]}  \t(elements № {i} and № {i + 1})')
