t=int(input())
while t>0:
    n=int(input())
    s=input()
    m=0
    for i in range(0,len(s)):
        c=0
        for j in range(0,len(s)):
            if s[i]==s[j]:
                c=c+1
        if c==1:
            m=1
            print(s[i])
            break
    if m==0:
        print("-1")
    t=t-1