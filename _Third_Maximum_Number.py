n=int(input())
a=list(map(int,input().split()))
c=sorted(a)
k=[]
for i in c:
    if i not in k:
        k.append(i)
if len(k)>=3:
    l=len(k)-2
    for i in range(0,len(k)):
        if k[i]==l:
            print(l)
            break
else:
    print(max(k))