t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                x=a[i]
                a[i]=a[j]
                a[j]=x
                s=s+1
    if s==0:
        print("0")
    else:
        k=a[n-1]-a[0]
        print(k)
    t=t-1    