n=int(input())
l=n
mi=0
ma=0
su=0
s=0
for i in range(n-1,0,-1):
    k=i
    su=0
    while k>0:
        r=k%10
        su=su*10+r
        k=k//10
    if su==i:
        mi=i
        break
for j in range(n+1,10000,1):
    p=j
    s=0
    while p>0:
        r=p%10;
        s=s*10+r
        p=p//10
    if s==j:
        ma=j
        break
c=l-mi
d=ma-l
if c>d:
    print(ma)
elif d>c:
    print(mi)
else:
    print(mi,ma,end=" ")