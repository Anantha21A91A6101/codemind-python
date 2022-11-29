n=int(input())
a=list(map(int,input().split()))
c=0
k=10000
l=0
t=0
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if a[i]==a[j]:
            c=c+1
    if c==a[i]:
        if a[i]<k:
            k=a[i]
        elif a[i]>l:
            l=a[i]
        t=t+1
if t==0:
    print("-1")
else:
    print(k,l,end=" ")