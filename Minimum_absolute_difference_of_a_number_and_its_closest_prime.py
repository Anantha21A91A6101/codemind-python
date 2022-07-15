n=int(input())
c=0
m=0
min=0
max=0
d1=0
d2=0
for i in range(1,n+1,1):
    if n%i==0:
        c=c+1
if c==2:    
    print("0")
else:
    for i in range(n,1,-1):
        c=0
        for j in range(1,i+1,1):
            if i%j==0:
                c=c+1
        if c==2:
            min=i
            break
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
        print(d2)
    else:
        print(d1)