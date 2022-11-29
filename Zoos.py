n=input()
x=0
y=0
for i in range(0,len(n)):
    if n[i]=='z':
        x=x+1
    if n[i]=='o':
        y=y+1
if 2*x==y:
    print("Yes")
else:
    print("No")