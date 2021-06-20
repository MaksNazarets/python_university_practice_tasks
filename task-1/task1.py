def is_number(char):
    return char in [str(i) for i in range(10)]


def is_last_or_first(char):
    separators = [" ", ",", ".", "+", "=", "/", "\\", "?", "!", "<", ">", "(", ")", ";", ":", "\"", "&", "№"]
    return char in separators or char in separators
    

init_string = input("Enter the string: ")
temp_string = str()
final_string = str()
numbers = []
final_numbers = []

for char in init_string:
    if is_number(char):
        numbers.append(int(char))
    else:
        temp_string += char

print(f'\n"Clear" string: {temp_string}\nThe numbers from the string: {numbers}')

for id, char in enumerate(temp_string):
    if id == 0 or id == len(temp_string) - 1 or is_last_or_first(temp_string[id + 1]) or is_last_or_first(temp_string[id - 1]):
        final_string += char.upper()
    else:
        final_string += char

print("Finish string:", final_string)
print("Max number of the array:", max(numbers))

for id, number in enumerate(numbers):
    if number != max(numbers):
        final_numbers.append(number ** id)

print("Final numbers list:", final_numbers)
