a=[]
while True:
    num=input("Please Enter a number")
    if num=="":
        break
    try:
        a.append(int(num))
    except ValueError:
        print("I said enter a number!")
print("top 5 number")
print(sorted(a,reverse=True)[:5])
    