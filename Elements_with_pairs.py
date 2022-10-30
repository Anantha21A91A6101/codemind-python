n=int(input())
a=list(map(int,input().split()))
if n%2==0:
    for i in range(0,len(a)):
        print(a[i],end=" ")
else:
    for i in range(0,len(a)):
        print(a[i],end=" ")
    print("0")