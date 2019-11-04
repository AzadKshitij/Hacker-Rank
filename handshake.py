import math
n = int(input())
k = []
for j in range(n):
    t = int(input())
    k.append(t)
    k = k
for i in k:
    if i == 1:
        print(0)
    elif i>1:
        ic2 = (math.factorial(i))/((math.factorial(i-2))*(math.factorial(2)))
        print("%.0f" % ic2)

