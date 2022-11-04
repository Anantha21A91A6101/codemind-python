n=int(input())
k=n-1
for i in range(0,n):
    for j in range(0,n):
        if j==0 or i==j or i+j==k:
            print("*",end=" ")
        else:
            print("  ",end="")
    k=k+1
    print(end="
")
    