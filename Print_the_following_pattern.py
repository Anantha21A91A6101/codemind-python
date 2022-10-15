n=int(input())
t=n
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if i==j or i+j==n+1:
            print(t,end=" ")
        else:
            print(end=" ")
    t=t-1
    print(end="
")    