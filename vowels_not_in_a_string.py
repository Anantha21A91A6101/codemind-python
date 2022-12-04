n=input()
n=n.lower()
n=n.split()
c=[]
k='aeiou'
m=0
d=[]
for i in n:
    for j in i:
        if j in k:
            c.append(j)
for i in k:
    if i not in c:
        d.append(i)
        m=m+1
if m==0:
    print("0")
else:
    l=sorted(d)
    print(*d)