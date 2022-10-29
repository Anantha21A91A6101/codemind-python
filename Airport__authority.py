n=int(input())
a=[]
for i in range(0,n):
    l=int(input())
    a.append(l)
k=int(input())
c=0
for i in a:
    if i<=k:
        c=c+1
    else:
        c=c+2
print(c)