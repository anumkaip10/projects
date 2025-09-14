# Input the lengths of three sides of a triangle. Check if it is Equilateral, Isosceles, or Scalene.
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))
if a == b == c:
    print("The Side of Triangle is Equilateral!")
elif a == b or b == c or c == a:
    print("The Side of Triangle is Isosceles")
else:
    print ("The Side of Triangle is scalene")