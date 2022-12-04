n=input()
n=n.split()
c=[]
b=[]
m=0
for i in n:
    for j in i:
        if j in 'aeiouAEIOU':
            c.append(j)
for i in c:
    if i not in b:
        b.append(i)
        m=m+1
if m==0:
    print("-1")
else:
    print(*b)