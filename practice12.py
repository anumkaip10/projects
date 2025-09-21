s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

cities = {"tokyo", "Madrid", "berlin", "Madrid"}
cities2 = {"tokyo", "Seoul", "kabul", "Madrid"}
cities3 = cities.union(cities2) 
print(cities3)

cities = {"tokyo", "Madrid", "berlin", "Madrid"}
cities2 = {"tokyo", "Seoul", "kabul", "Madrid"}
cities3 = cities.update(cities2) 
print(cities3)

cities = {"tokyo", "Madrid", "berlin", "Madrid"}
cities2 = {"tokyo", "Seoul", "kabul", "Madrid"}
cities3 = cities.intersection(cities2) 
print(cities3)

cities = {"tokyo", "Madrid", "berlin", "Madrid"}
cities2 = {"tokyo", "Seoul", "kabul", "Madrid"}
cities3 = cities.update(cities2) 
print(cities3)

cities = {"tokyo", "Madrid", "berlin", "Madrid"}
cities2 = {"tokyo", "Seoul", "kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2) 
print(cities3)

cities = {"tokyo", "Madrid", "berlin1", "Madrid2"}
cities2 = {"tokyo", "Seoul", "kabul", "Madrid"}
cities3 = cities.isdisjoint(cities2) 
print(cities3)

cities = {"tokyo", "Madrid", "berlin", "Madrid"}
cities2 = {"tokyo", "Seoul", "kabul", "Madrid"}
cities3 = cities.issuperset(cities2) 
print(cities3)

cities = {"tokyo", "Madrid", "berlin", "Madrid"}
cities2 = { "tokyo", "Madrid", "delhi"}
cities3 = cities.issubset(cities2) 
print(cities3)

cities = {"tokyo", "Madrid", "berlin"}
cities.add("helsinki") 
print(cities)

cities = {"tokyo", "Madrid", "berlin", "delhi"}
cities.remove("tokyo")
print(cities)

cities = {"tokyo", "Madrid", "Berlin", "delhi"}
cities.discard("Tokyo2")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

cities = {"Tokyo", "Madrid", "berlin", "Delhi"}
del cities
print(cities2)

cities = {"tokyo", "Madrid", "berlin", "Delhi"}
cities.clear
print(cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is persent.")
else:
    print("Carla is absent")