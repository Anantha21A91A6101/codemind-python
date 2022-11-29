t=int(input())
while t>0:
    s=input()
    c=0
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            c=c+1
    print(c)
    t=t-1