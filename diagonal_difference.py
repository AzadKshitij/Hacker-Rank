n = int(input())
l = []
for i in range(n):
    a = list(map(int,input().split(sep=" ", maxsplit=n)))
    l.append(a)
sum_1 = 0
sum_2 = 0
for i in range(n):
    sum_1 = sum_1 + l[i][i]
    sum_2 = sum_2 + l[i][n-1-i]

diff = sum_1 - sum_2
if diff >=0:
    print(diff)
else: print(-diff)
