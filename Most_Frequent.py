n=int(input())
a=list(map(int,input().split()))
c=0
m=0
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if a[i]==a[j]:
            c=c+1
    if c>m:
        m=c
        k=a[i]
    elif c==m:
        if k>a[i]:
            k=a[i]
print(k)