n=input()
n=n.split()
c=[]
d=[]
b=[]
e=[]
for i in n:
    for j in i:
        if j in 'aeiou':
            c.append(j)
        if j in 'AEIOU':
            d.append(j)
for i in c:
    if i not in b:
        b.append(i)
for j in d:
    if j not in e:
        e.append(j)
if len(b)==5 or len(e)==5:
    print("True")
else:
    print("False")