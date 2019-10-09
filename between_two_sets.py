n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
l = []
p = []
t = []
d = []
for j in a:
    for i in range(max(a) ,min(b)+1):
        if i%j == 0:
            l.append(i)
for i in l:
    if i not in t:
        t.append(i)
for j in a:
    for i in range(max(a) ,min(b)+1):
        if i%j!=0 and i in t:
            t.remove(i)
for k in b:
    for g in t:
        if k%g == 0:
            p.append(g)
for i in p:
    if i not in d:
        d.append(i)
for k in b:
    for g in t:
        if k%g!=0 and g in d:
            d.remove(g)
print(len(d))
