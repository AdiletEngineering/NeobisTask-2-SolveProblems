print("please type words separated by space | limit 100 symbols")
string1 = input(str())
if len(string1) > 100:
	print("строка превышает 100 символов")
else:
	print("-------------------------------------------------------------------")
	array = string1.split(" ")
	for i in range(len(array)):
		print(f"{i+1}: {'   '*i}{array[i]}")
		# print("\t"*i + array[i])                  ##another way
