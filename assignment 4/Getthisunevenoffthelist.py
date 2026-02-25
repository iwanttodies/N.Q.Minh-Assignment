def filter(number):
    list2=[]
    for i in number:
        if i%2==0:
            list2.append(i)
    return list2
list=[]
while True:
    mumber=input("enter your number(empty to stop): ")
    if mumber==(""):
        break
    list.append(int(mumber))
evenlist=filter(list)
print(f"The Og list: {list}")
print(f"The new list: {evenlist}") 
    