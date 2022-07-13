m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=set(a)
d=set(b)
k=0
for i in c:
    if i not in d:
        k=k+1
for i in d:
    if i not in c:
        k=k+1
print(k)        