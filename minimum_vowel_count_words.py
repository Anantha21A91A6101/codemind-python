n=input()
n=n.split()
d=[]
k=0
for i in n:
    c=0
    for j in i:
        if j in 'aeoiAEIOU':
            c=c+1
    d.append(c)
if len(d)==1:
    print("1")
else:
    k=min(d)
    print(d.count(k))