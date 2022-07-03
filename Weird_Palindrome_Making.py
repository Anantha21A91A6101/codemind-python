t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    m=0
    for i in range(n):
        if a[i]%2!=0:
            c=c+1
        else:
            m=m+1
    print(int(c/2))
    t=t-1