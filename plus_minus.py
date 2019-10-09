greater = 0
lesser = 0
equal = 0
n = int(input())
array = list(map(int,input().split(sep=" ", maxsplit=n)))
for i in range(0,n):
    if array[i]> 0 :
        greater = greater + 1
    elif array[i]< 0:
        lesser = lesser + 1
    else:
        equal = equal + 1
print(greater/n)
print(lesser/n)
print(equal/n)
