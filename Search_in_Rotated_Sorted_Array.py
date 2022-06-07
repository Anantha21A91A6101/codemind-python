n=int(input())
a=list(map(int,input().split()))
k=int(input())
m=0
for i in range(0,len(a)):
    if a[i]==k:
        print(i,end='')
        m=m+1
if m==0:
    print(-1)
    