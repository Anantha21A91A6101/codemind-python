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
    for j in s2:
        if i==j:
            c.append(j)
            m=1
if m==0:
    print("-1")
else:
    from collections import OrderedDict
    k=sorted(c)
    k="".join(OrderedDict.fromkeys(k))
    for i in k:
        print(i,end="")