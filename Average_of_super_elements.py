n=int(input())
a=list(map(int,input().split()))
sum=0
m=0
k=0
d=0
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if a[i]==a[j] and a[i]!=-1:
            c=c+1
    if c==a[i]:
        sum=sum+a[i]
        a[i]=-1
        m=m+1
if m==0:
    print("-1")
else:    
    k=sum/m
    d="{:.2f}".format(k)
    print(d)
    