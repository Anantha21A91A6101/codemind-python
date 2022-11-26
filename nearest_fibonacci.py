n=int(input())
a=0
b=1
c=a+b
if n==0:
    print("0")
else:
    while c<=n:
        a=b
        b=c
        c=a+b
    k=abs(c-n)
    l=abs(b-n)
    if k>l:
        print(b,end="")
    elif k<l:
        print(c,end="")
    else:
        print(b,c,end=" ")