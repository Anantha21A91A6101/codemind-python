t=int(input())
while t>0:
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    k=0
    l=0
    for i in range(0,len(a)):
        sum=0
        for j in range(i,len(a)):
            sum=sum+a[j]
            if sum==m:
                k=i+1
                l=j+1
                c=1
                break
        if c==1:
            break
    if c==0:
        print("-1")
    else:
        print(k,l,)
    t=t-1
                