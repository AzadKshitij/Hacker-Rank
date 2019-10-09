n = int(input())
number = list(map(int,input().split(sep=" ",maxsplit=n)))
sum_ = 0
for i in range(0,len(number)):
    sum_ = sum_ + number[i]
print(sum_) 
