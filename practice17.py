def func1():
 try:
    l = [1,5,6,7]
    i = int(input("Enter the index: "))
    print(l(i))
    return 1
 except:
    print("some error accurred")
    # finally:
    # print("I am always Executed")

x = func1()
print (x)