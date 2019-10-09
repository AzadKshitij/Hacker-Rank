n = int(input())
scores = list(map(int,input().split()))
broke=scores[0]
worst=scores[0]
broke_score = worst_score = 0
for i in range(len(scores)):
    if scores[i]>broke:
        broke = scores[i]
        broke_score+=1
    if scores[i]<worst:
        worst = scores[i]
        worst_score+=1
print(broke_score,worst_score)
