n = int(input())
arry = list(map(int,input().split()))
lists = list(map(int,input().split()))
d = lists[0]
m = lists[1]
count =0
for i in range(0,n):
    length = 0
    sum_=0
    for j in range(i,n):
        length=length+1
        sum_=sum_+ arry[j]
        if length == m and sum_ == d:
            count=count+1
            break
        if sum_ > d or length > m:
            break
        j+=1
    i+=1
print(count)
