from functools import reduce
l=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1]
blue=reduce(lambda x,y:x+y,l)
print(blue)
