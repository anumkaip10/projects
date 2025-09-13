# Input three numbers and print the largest number
a = int(input("Enter first Number:"))
b = int(input("Enter second Number"))
c = int(input("Enter second Number"))

if a >= b and a >= c:
  print(a, "is the largest Number")
elif b >= a and b >= c:
    print(b,"is the largest Number")
else:
    print(c,"is the Largest Number")

