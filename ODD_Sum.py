n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
    if a[i]%2!=0:
        c=c+a[i]
print(c,end='')        