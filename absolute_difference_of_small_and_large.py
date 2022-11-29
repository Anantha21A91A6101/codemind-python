n=input()
n=n.split()
for i in range(0,len(n)):
    k=ord(max(n[i]))
    l=ord(min(n[i]))
    print(abs(k-l),end=" ")