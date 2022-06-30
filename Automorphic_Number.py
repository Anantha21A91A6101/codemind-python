n=int(input())
c=0
h=n
sq=n*n
while n>0:
    r=n%10
    c=c+1
    n=n//10
m=pow(10,c)
k=sq%m
if k==h:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")