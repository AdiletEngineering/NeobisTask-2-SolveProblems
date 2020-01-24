from pprint import pprint

string = input("Введите Час, Минуты, Секунды через пробел: ")
array = string.split(" ")

h = int(array[0])
m = int(array[1])
s = int(array[2])

sec = (h*60*60) + (m*60) + s
pprint(sec)
