n=int(input())
a=list(map(str,input().split()))
l=[]
for i in a:
    l.append(len(i))
print(l.count(max(l)))    