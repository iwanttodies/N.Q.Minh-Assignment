def sum2(number):
    total=0
    for i in number:
        total+=i
    return total
thelist=[]
while True:
    theinput=((input("enter your number(empty to stop): " )))
    if theinput==(""):
        break
    thelist.append(int(theinput))
    
result=sum2(thelist)
print(f"your sum is {result}")