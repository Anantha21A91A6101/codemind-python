n=int(input())
a=list(map(int,input().split()))
k=0
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if a[i]==a[j]:
            c=c+1
    if c>k:
        k=c
        m=a[i]
print(m,end='')        
        