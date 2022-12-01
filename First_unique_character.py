n=input()
n=n.split()
n="".join(n)
c=0
m=0
for i in n:
    c=0
    for j in n:
        if i==j:
            c=c+1
    if c==1:
        print(i)
        m=1
        break
if m==0:
    print("-1")