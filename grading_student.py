n = int(input())
l= []
for i in range(n):
    num = int(input())
    l.append(num)
    for j in range(1,3):
        if l[i]%5!=0 and l[i]>=38:
            if (l[i]+j)%5==0:
                l[i]=l[i]+j
            else:
                l[i]=l[i]
for k in range(n):
    print(l[k])
