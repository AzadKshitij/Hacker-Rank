n = int(input())
l = []
for i in range(n):
    px, py, qx, qy = map(int, input().split())
    rx = (2*qx) - px
    ry = (2*qy) - py
    l.append(rx)
    l.append(ry)
for i in range(0, 2*n, 2):
    A = l[i]
    B = l[i+1]
    print(A, B)
