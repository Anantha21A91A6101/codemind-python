n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
r=[]
for i in a:
    if i in b:
        c.append(i)
for i in c:
    if i not in r:
        r.append(i)
print(*r)