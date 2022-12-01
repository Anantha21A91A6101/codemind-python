n=input()
n=n.lower()
n=n.split()
n="".join(n)
m=0
c=0
for i in n:
    c=0
    for j in n:
        if i==j:
            c=c+1
    if c==1:
        m=m+1
print(m)