# ask for the person age and check, if age<13(child), 13<19(teenager), 20<59(Adult), 60+ (Senior citizen)
a = int(input("Enter your age: "))
if(a<13):
    print("Your a child!")
elif 13 <= a <= 19:
    print("Your a Teenager!")
elif 20 <= a <= 59:
    print("Your a Adult")
else:
    print("Your a Senior Citizen")

