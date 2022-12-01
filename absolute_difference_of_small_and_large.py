n=input()
n=n.split()
s=0
d=0
for i in n:
    k=ord(max(i))
    l=ord(min(i))
    print(abs(k-l),end=" ")