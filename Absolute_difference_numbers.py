n,k=map(int,input().split())
h=n
c=0
sum=0
p=0
add=0
w=0
m=0
while n>0:
    r=n%10
    c=c+1
    sum=sum*10+r
    if c==k:
        break
    n=n//10
while sum>0:
    r=sum%10
    add=add*10+r
    sum=sum//10
while h>0:
    r=h%10
    w=w*10+r
    h=h//10
while w>0:
    r=w%10
    m=m+1
    p=p*10+r
    if m==k:
        break
    w=w//10
s=abs(add-p)  
print(s)