import math
from pprint import pprint

inp = list(map(float, input().split(" ")))

def distance_formula(x1, y1, x2, y2):
	AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return AB

ab = distance_formula(inp[0], inp[1], inp[2], inp[3])
bc = distance_formula(inp[2], inp[3], inp[4], inp[5])
ac = distance_formula(inp[0], inp[1], inp[4], inp[5])
P = ab + bc + ac #perimeter
p = P / 2 #half of perimeter
S = math.sqrt(p*(p-ab)*(p-bc)*(p-ac))

print("perimetr:", P,"area:", S)
