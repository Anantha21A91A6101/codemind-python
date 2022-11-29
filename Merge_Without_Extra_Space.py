t=int(input())
while t>0:
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for i in range(0,len(a)):
        c.append(a[i])
    for j in range(0,len(b)):
        c.append(b[j])
    k=sorted(c)
    print(*k)
    t=t-1