for i in range(12):
    if (i == 10):
        print("Skip the iteration")
        continue
    print("5 x", i, "=", 5*i)
for i in range(12):
    print("5 x", i, "=", 5*i)
    if(i == 10):
        break
