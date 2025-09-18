marks = [3,5,6,7,9]
print(marks)
print(type(marks[0]))
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3])
print(marks[5-3])
print(marks[2])

if 7 in marks:
    print("yes")
else:
    print("no")
    
if "an" in "Anum":
    print("yes")

print(marks)
print(marks[1:-1])
print(marks[1:-4])

print (marks)
print(marks[1:-1])
print(marks[1:4])

lst = [1 for i in range(4)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print (lst)