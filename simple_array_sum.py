n = int(input())
k = map(int,input().split(sep=" ", maxsplit=n))
x = 0
for i in k:
    x = x + i
print(x)
