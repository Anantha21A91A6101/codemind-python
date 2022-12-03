n=input()
v=len(n)
k=0
c=[]
for i in n:
    if i=='I':
         c.append(k)
         k=k+1
    else:
        c.append(v)
        v=v-1
for i in range(1,v+1):
    if i not in c:
        c.append(i)
        break
print(*c)