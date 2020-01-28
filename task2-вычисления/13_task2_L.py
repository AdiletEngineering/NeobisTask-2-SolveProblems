inp = list(map(int, input().split(" ")))

n = inp[0]
x1 = inp[1]
d = inp[2]

xn = x1 + ((n-1) * d)
average = ((n * (x1 + xn))/2) / n

print(int(average))
