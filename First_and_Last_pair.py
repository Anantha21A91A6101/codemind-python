n=int(input())
a=list(map(int,input().split()))
k=n//2
c=[]
d=[]
m=0
l=0
if n%2!=0:
    for i in range(0,len(a)):
        if k>=m:
            c.append(a[i])
            m=m+1
    for j in range(len(a)-1,-1,-1):
        if k>l:
            d.append(a[j])
            l=l+1
else:
    for i in range(0,len(a)):
        if k>m:
            c.append(a[i])
            m=m+1
    for j in range(len(a)-1,-1,-1):
        if k>l:
            d.append(a[j])
            l=l+1
i=0
j=0
while i<len(c) or j<len(d):
    if i<len(c):
        print(c[i],end=" ")
        i=i+1
    if j<len(d):
        print(d[j],end=" ")
        j=j+1
if n%2!=0:
    print(0)