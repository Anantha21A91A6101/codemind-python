n=int(input())
a=list(map(int,input().split()))
c=0
d=[]
for i in range(0,len(a)):
    if a[i]==1:
        c=c+1
    else:
        c=0
    d.append(c)
print(max(d))