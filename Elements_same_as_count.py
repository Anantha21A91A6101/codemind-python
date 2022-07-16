n=int(input())
a=list(map(int,input().split()))
m=0
c=0
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if a[i]==a[j] and a[i]!=-1:
            c=c+1
    if c==a[i]:
        print(a[i],end=" ")
        a[i]=-1
        m=m+1
if m==0:
    print("-1")
    