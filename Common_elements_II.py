m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(0,len(a)):
    if a[i] not in b:
        c.append(a[i])
for j in range(0,len(b)):
    if b[j] not in a:
        c.append(b[j])
print(*c)        