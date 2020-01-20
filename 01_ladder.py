print("please type words separated by space")
string1 = input(str())
print("-------------------------------------------------------------------")

array = string1.split(" ")
for i in range(len(array)):
	print("\t"*i + array[i])
