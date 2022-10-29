t=int(input())
while t>0:
    n,m=map(int,input().split())
    y=-1
    for i in range(0,m,1):
        if i*i%m==n:
            y=i
            break
    print(y)
    t=t-1