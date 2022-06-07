n=int(input())
a=list(map(int,input().split()))
k=int(input())
m=0
n=0
for i in range(0,len(a)):
    if a[i]==k:
        print(i,end=' ')
        n=n+1
        break
for j in range(len(a)-1,-1,-1):
    if a[j]==k:
        print(j,end='')
        m=m+1
        break
if m==0 and n==0:
    print(-1,-1)