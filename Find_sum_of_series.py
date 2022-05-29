a=int(input())
sum=0
for i in range(1,a+1,1):
    sum=sum+(1.0/i)
k="{:.2f}".format(sum)
print(k)