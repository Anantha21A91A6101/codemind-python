n=int(input())
l=list()
while n>0:
    r=n%10
    l.append(r)
    n=n//10
for i in range(len(l)-1,-1,-1):
    if l[i]==6:
        l[i]=9
        break
for i in range(len(l)-1,-1,-1):
    print(l[i],end="")