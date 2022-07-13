t=int(input())
while t>0:
    n=int(input())
    for i in range(n,1,-1):
        c=0
        for j in range(1,i+1,1):
            if i%j==0:
                c=c+1
        if c==2:
            min=i;
            break;
    for k in range(n+1,100000,1):
        c=0
        for m in range(1,k+1,1):
            if k%m==0:
                c=c+1
        if c==2:
            max=k
            break
    d1=abs(n-min)
    d2=abs(n-max)
    if d1>d2:
        print(max,end="
")
    else:
        print(min,end="
")
    t=t-1    