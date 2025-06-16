tup=(1,2,76,342,32,"green", True)
print(type(tup),tup)
print(tup[0])
print(tup[-1])

if 342 in tup:
     print("Yes 342 is present in this tuple")
else:
    print("It is absent")
    
tup2=tup[1:4]
print(tup2)

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

countries=("pakistan","USA","Nepal")
countries2=("Qatar","India","China")
detail=countries+countries2
print(detail)

# Count methos in tuple(types of methods)
tuple1=(0,1,2,3,4,3,5,6,3,7,3,8)
res=tuple1.count(3)
print('Count of 3 in tuple1 is:',res)

# index method()
tuple1=(0,1,2,4,3,3,5,6,3,7,3,8)
res=tuple1.index(3)
print('Index of 3 in tuple1 is:',res)

# Unpack Tuples
info = ("Dipti", 20, "VS International College")
(name, age, university) = info
print("Name:", name)
print("Age:",age)
print("Studies at:",university)

info = {"Carla", 19, False, 5.9, 19}
print(info)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)




