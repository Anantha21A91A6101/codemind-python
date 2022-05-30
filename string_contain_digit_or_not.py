a=input()
sum=0
for i in a:
    if i.isdigit()==True:
        sum=sum+1
if sum!=0:
    print("Contains",sum,"digit")
else:
    print("Doesn't", "contain", "digit")