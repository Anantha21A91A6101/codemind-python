n=int(input())
t=n
c=0
m=0
s=0
for i in range(1,t+1,1):
    if t%i==0:
        c=c+1
if c==2:
    while n:
        r=n%10
        m=m+1
        n=n//10
        k=0
        for i in range(1,r+1,1):
            if r%i==0:
                k=k+1
        if k==2:
            s=s+1
if c==2 and s==m:
    print("Mega Prime")
elif c>2 or s!=m:
    print("Not Mega Prime")