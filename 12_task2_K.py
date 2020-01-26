inp = list(map(int, input().split(" ")))

n = inp[0]
m = inp[1]
breaks = (n-1)+((m-1)*n)

print(breaks)
