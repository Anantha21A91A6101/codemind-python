n,b=map(int,input().split())
a=list(map(int,input().split()))
t=0
c=0
for i in range(len(a)):
    c=0
    k=a[i]
    if k==0:
        c=c+1
    else:
        if k>0:
            while k:
                k=k//10
                c=c+1
        elif k<0:
            r=-(a[i])
            while r:
                r=r//10
                c=c+1
    if c==b:
        t=t+1
        c=0
print(t)