countries = ("Spain", "Italy", "India","pakistan", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

countries = ("pakistan", "Afganistan", "bangladesh", "Sirilanka")
countries2 = ("Vietnam", "india","china")
southEastAsia = countries + countries2 
print(southEastAsia)

tuple1 = (0,1, 2, 3, 2, 3, 1, 3, 2, 3)
res = tuple1.count(3)
print('Count of 3 in tuple1 is:',res)

tuple2= (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res = tuple2.index(3)
print('Index of 3 in tuple2 is:', res)

tuple3 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res = tuple3.index(3, 4, 8)
print('Index of 3 in tuple3 is:',res)




       
