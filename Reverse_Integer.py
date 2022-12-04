n=int(input())
c=0
sum=0
if n<0:
    n=-(n)
    c=c+1
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
if c==1:
    sum=-(sum)
    print(sum)
else:
    print(sum)