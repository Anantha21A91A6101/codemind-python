n=int(input())
a=list(map(int,input().split()))
c=n-1
sum=0
for i in range(0,len(a)):
    k=a[i]
    sum=sum+(2**c)*k
    c=c-1
print(sum)    