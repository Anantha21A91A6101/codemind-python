s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=s1.split()
s2=s2.split()
s1="".join(s1)
s2="".join(s2)
c=[]
m=0
for i in s1:
    m=0
    for j in s2:
        if i==j:
            m=m+1
    if m==0:
        c.append(i)
for j in s2:
    m=0
    for i in s1:
        if j==i:
            m=m+1
    if m==0:
        c.append(j)
from collections import OrderedDict
k=sorted(c)
k="".join(OrderedDict.fromkeys(k))
print(len(k))