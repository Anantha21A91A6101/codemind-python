n=input()
n=n[::-1]
n=n.split()
for i in n:
    s=min(i)
    break
m=s.lower()
k=0
for i in n:
    if m in i:
        print(m)
        k=1
        break
if k==0:
    print(s)