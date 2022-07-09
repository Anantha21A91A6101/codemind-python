n=int(input())
a=list(map(str,input().split()))
a1=[]
a2=[]
for i in a:
    a1.append(len(i))
for i in range(n):
    if a1[i]==max(a1):
        a2.append(a[i])
print(*a2)        