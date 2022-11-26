s=input()
c=0
m=0
for i in range(0,len(s)):
    c=0
    for j in range(0,len(s)):
        if i!=j:
            if s[i]==s[j]:
                c=c+1
    if c==0:
         print(s[i])
         m=1
         break
if m==0:
    print("-1")
            