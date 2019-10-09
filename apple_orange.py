s,t = map(int,input().split())
a,b = map(int,input().split())
m,n = map(int,input().split())
app = list(map(int,input().split()))
orng= list(map(int,input().split()))
num_a = 0
num_o = 0
for i in app:
    if s<=i+a<=t:
        num_a+=1
for j in orng:
    if s<=j+b<=t:
        num_o+=1
print(num_a)
print(num_o)
