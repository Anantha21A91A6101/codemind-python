m=int(input())
n=int(input())
for i in range(m,n+1,1):
    k=i
    sum=0
    while k!=0:
        r=k%10
        sum=sum*10+r
        k=k//10
    if sum==i:
        print(sum,end=' ')
        