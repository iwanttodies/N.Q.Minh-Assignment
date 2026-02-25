city=[]
for i in range(1,6):
    name=input(f"Enter city num {i}: ")
    city.append(name)
print("top 5 cities(according to you)")
for name in city:
    print(f"-{name}")