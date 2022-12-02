n=input()
c=[]
b=[]
s=0
for i in n:
    if i in 'aeiouAEIOU':
        c.append(i)
for i in c:
    if i not in b:
        b.append(i)
        s=s+1
if s==0:
    print("-1")
else:
    print(*b)