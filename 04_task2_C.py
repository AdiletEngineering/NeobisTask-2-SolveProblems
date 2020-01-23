from pprint import pprint

string = input("Введите трехзначное число: ")
array = []
for i in string:
	array.append(int(i))
pprint(array)