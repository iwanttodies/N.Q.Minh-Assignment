num=int(input("Please enter a number "))
if num<2:
    print("prime number but small")
for i in range (2,num-1):
    if num%i==0:
        print("Not prime good sir")
    else:
        print("Prime number good sir")
        break