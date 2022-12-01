n=input()
n=n.lower()
n=n.split()
k='aeiou'
c=[]
d=[]
for i in n:
    for j in i:
        if j in k:
            d.append(j)
for i in k:
    if i not in d:
        c.append(i)
if c==[]:
    print("0")
else:
    k=sorted(c)
    print(*k)