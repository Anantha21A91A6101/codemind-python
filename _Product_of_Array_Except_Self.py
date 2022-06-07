n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)):
    c=1
    for j in range(0,len(a)):
        if a[i]!=a[j]:
            c=c*a[j]
    print(c,end=' ')