import math

string1 = input("введите координаты (x1, y1) для точки A через пробел: ")
string2 = input("введите координаты (x2, y2) для точки B через пробел: ")

array1 = string1.split(" ")
array2 = string2.split(" ")

x1 = int(array1[0])
y1 = int(array1[1])
x2 = int(array2[0])
y2 = int(array2[1])

print("---------------------------------------------")
print(f"координаты точки A: ({x1}, {y1})")
print(f"координаты точки B: ({x2}, {y2})")

AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Расстояние между точками A и B составляет: {AB}")
