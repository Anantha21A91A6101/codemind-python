n=int(input())
a=list(map(int,input().split()))
c=a[0]
for i in range(0,len(a)):
    if a[i]>=c:
        c=a[i]
print(c)        
        