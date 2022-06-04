n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
    k=a[i]
    sum=0
    while k>0:
        r=k%10
        sum=sum*10+r
        k=k//10
    if sum==a[i]:
        c=c+1
print(c,end='')        