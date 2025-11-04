
def greet(fx):
 def mfx(*args, **kwargs):
  print("Good Moring")
  fx(*args, **kwargs)
 print("thanks for using this function")
 return mfx


@greet
def hello():
  print("Hello World")

# @greet
def add(a, b):
   print(a+b)


# greet(hello)()
hello()
greet(add)(1,2)