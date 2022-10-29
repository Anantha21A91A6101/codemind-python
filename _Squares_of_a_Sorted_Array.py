n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,len(a)):
    k=a[i]*a[i]
    l.append(k)
m=sorted(l)
for j in m:
    print(j,end=" ")