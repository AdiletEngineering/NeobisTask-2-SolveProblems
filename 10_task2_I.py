inp = list(map(int, input().split(" ")))

a1 = inp[0]
a2 = inp[1]
d = a2 - a1
n = inp[2]

print(a1 + (n - 1) * d)
