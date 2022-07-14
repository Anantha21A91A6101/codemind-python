n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=set(a)
d=set(b)
c=0
for i in k:
    if i in d:
        c=c+1
print(c)        