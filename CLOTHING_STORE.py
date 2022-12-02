n=int(input())
a=list(map(int,input().split()))
m=0
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if a[i]==a[j] and a[i]!=-1:
            c=c+1
    if c%2==0:
        m=m+1
    a[i]=-1
print(m)