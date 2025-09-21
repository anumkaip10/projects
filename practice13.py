dic = {
    "Anum": "Human being",
    "spoon": "Object"

}

print(dic["Anum"])

dic = {
   
    344: "Anum",
    56: "Fatima",
    678: "Ali",
    549: "Ahmed"
}
  
print(dic[678])

info = {"name" : 'Ali', 'age':19, 'eligible': True}
print(info)
print(info['name'])
print(info.get('eligible'))

info = {"name : 'Ali, 'age":19,'eligible':True}
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"The value of the key {key} is {info[key]}")


