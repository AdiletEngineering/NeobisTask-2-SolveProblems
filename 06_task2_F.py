from pprint import pprint

seconds = int(input("Введите секунды: "))

hours = seconds // 3600

seconds = seconds % 3600
minutes = seconds // 60

seconds = seconds % 60

print(hours, minutes, seconds)
