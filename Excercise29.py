X = 3
print(X)

def hello():
    X = 4
    print(f"the local X starts with {X}")
    print(X)
    print("hello AK")
    print(f"the global X starts from {globals()['X']}")

hello()
print(f"the global X starts from {X}")
