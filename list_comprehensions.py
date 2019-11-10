
x = int(input())
y = int(input())
z = int(input())
n = int(input())
X = []
Y = []
Z = []
l = []
for a in range(0,x+1):
    X.append(a)
for b in range(0,y+1):
    Y.append(b)
for c in range(0,z+1):
    Z.append(c)
for i in X:
    for j in Y:
        for k in Z:
            if (i+j+k) != n:
                l.append([i,j,k])
print(l)
