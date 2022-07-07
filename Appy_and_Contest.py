t=int(input())
while t>0:
    n,a,b,k=map(int,input().split())
    if a%b==0:
        l=a
    elif b%a==0:
        l=b;
    else:
        l=a*b;
    f=n//l;
    c=n//a;
    d=n//b;
    c=c-f;
    d=d-f;
    if c+d>=k:
        print("Win",end="
")
    else:
        print("Lose",end="
")
    t=t-1    