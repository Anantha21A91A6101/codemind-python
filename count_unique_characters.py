n=input()
n=n.lower()
n=n.split()
c=[]
m=0
s=0
for i in n:
    for j in i:
        c.append(j)
for i in range(0,len(c)):
    m=0
    for j in range(0,len(c)):
        if c[i]==c[j]:
            m=m+1
    if m==1:
        s=s+1
print(s)