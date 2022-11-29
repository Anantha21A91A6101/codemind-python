n=input()
n=n.split()
s=0
m=0
for i in range(0,len(n)):
    k=ord(max(n[i]))
    l=ord(min(n[i]))
    s=s+k
    m=m+l
print(abs(s-m))