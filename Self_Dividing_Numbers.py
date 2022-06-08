a=int(input())
b=int(input())
for i in range(a,b+1,1):
    k=i;
    while k>0:
        r=k%10
        if r==0 or i%r!=0:
            break
        k=k//10
    if k==0:
        print(i,end=' ')