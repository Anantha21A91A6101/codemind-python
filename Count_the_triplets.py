t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if i!=j:
                for k in range(0,len(a)):
                    if a[i]+a[j]==a[k]:
                        c=c+1
    if c==0:
        print("-1")
    else:
        print(c//2)
    t=t-1