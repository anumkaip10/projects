from operator import index  

marks = [1, 23, 44, 34, 12, 43, 45, 23, 97]
for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Anum, Awesome")
        index += 1


marks = [1, 23, 44, 34, 12, 43, 45, 23, 97]

for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Anum, Awesome")
