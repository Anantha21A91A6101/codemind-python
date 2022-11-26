n=input()
m=0
c=0
for i in range(0,len(n)):
    c=0
    for j in range(0,len(n)):
        if i!=j:
            if n[i]==n[j]:
                c=c+1
    if c==0:
        print(i)
        m=1
        break
if m==0:
    print("-1")