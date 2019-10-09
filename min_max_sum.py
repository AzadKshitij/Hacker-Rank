n = list(map(int,input().split()))
min_sum = 0
max_sum = 0
for i in range(0,len(n)):
    min_sum = min_sum + n[i] 
    max_sum = max_sum + n[i] 
min_sum = min_sum - max(n)
max_sum = max_sum - min(n)
print(min_sum,max_sum)
