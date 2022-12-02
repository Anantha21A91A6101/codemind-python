n=input()
n=n.split()
c=[]
k='aeiou'
l='AEIOU'
d=[]
w=0
r=0
for i in n:
    for j in i:
        if j in k:
            c.append(j)
        elif j in l:
            d.append(j)
from collections import OrderedDict
m="".join(OrderedDict.fromkeys(c))
s="".join(OrderedDict.fromkeys(d))
for i in k:
    if i in c:
        w=w+1
for j in l:
    if j in d:
        r=r+1
if w==5 or r==5:
    print("True")
else:
    print("False")