n=int(input())
a=list(map(int,input().split()))
d=[]
c=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        c.append(a[i])
    else:
        d.append(a[i])
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
    print("0")