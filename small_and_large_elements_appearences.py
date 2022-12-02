n=input()
n=n.split()
c=[]
s=0
w=0
for i in n:
    for j in i:
        c.append(j)
k=min(c)
l=max(c)
for i in c:
    if i in k:
        s=s+1
for j in c:
    if j in l:
        w=w+1
print(k,s,l,w)