n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)):
    if i%2==0:
        k=a[i]
        c=1
        if(i+1)%2!=0:
            while c<=k:
                print(a[i+1],end=" ")
                c=c+1