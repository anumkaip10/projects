a = input("Enter the number: ")
print("Multiplication table of {a} is: ")
try:
 for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print("invalid input")

    # print("some imp lines of code")
    # print("End of program")

try:
   num = int(input("Enter an integer: "))
except ValueError:
   print("number entered is not an integer")
except IndexError:
   print("index Error")

try:
   tup1 = (1,2,3,4,5)
   tup1.insert(2,9)
   print(tup1)
#    list1 = list(tup1)
# list1 = insert(2,9)
# tup1 = tuple(list1)
# print(tup1)
except AttributeError:
   print("No changes is made in tuple directly once they are created")

try:
   dic={"name": "rayees", "age":23, "roll no":12345454, "DOB": 24/6/1959}
#    print(dic["name"])
print(dict["adhaar"]) # type: ignore
exceptKeyError:
print("this key donot exist in dict")