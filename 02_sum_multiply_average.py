from pprint import pprint

string = input("Введите 3 цифры через пробел: ")
print("------------------------------------------------------------")

array = string.split(" ")
a = int(array[0])
b = int(array[1])
c = int(array[2])

sum = a + b + c
multiply = a * b * c
average = (a + b + c) / 3

print(f"{a}+{b}+{c} = {sum}")
print(f"{a}*{b}*{c} = {multiply}")
print(f"({a}+{b}+{c})/3 = {average}")
