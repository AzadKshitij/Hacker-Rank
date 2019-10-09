a = list(map(int,input().split()))
b = list(map(int,input().split()))
B = 0
A = 0
if a[0]>b[0]:
    A = A +1
elif a[0] == b[0]:
    A = A
    B = B
else:
    B+=1
if a[1]>b[1]:
    A = A +1
elif a[1] == b[1]:
    A = A
    B = B
else:
    B+=1
if a[2]>b[2]:
    A = A +1
elif a[2] == b[2]:
    A = A
    B = B
else:
    B+=1
print(A,B)
