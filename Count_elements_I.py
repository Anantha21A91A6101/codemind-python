n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
A=set(a)
B=set(b)
c=0
for i in A:
    if i in B:
        c=c+1
print(c)            