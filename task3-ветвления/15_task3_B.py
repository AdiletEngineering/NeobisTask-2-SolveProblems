from pprint import pprint

inp = list(map(int, input().split(" ")))
pprint(inp)

names = {
	"Anton1": inp[0],
	"Boris2": inp[1],
	"Victor3": inp[2]
}

if inp[0] == inp[1] == inp[2]:
	print("equal")
elif max(names.keys()):
	print("Anton")

print(names.keys(), names.values())