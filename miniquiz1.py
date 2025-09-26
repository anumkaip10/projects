a = int(input("Enter a value between 5 and 9: "))

if(a == "quite"):
    print("Thank You")
elif(int(a)<5 or int(a)>9):
    raise ValueError("The given item is invalid")
print("Thank You\nHave a Great Day")