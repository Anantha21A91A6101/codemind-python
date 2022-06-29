n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
        c=c+a[i]
print(c,end='')        