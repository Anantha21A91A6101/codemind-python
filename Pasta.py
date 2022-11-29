n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=0
c=0
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[i]:
            c=c+1
    if c>0:
        x=x+1
if x>0:
    print("Yes")
else:
    print("No")