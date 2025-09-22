for i in range(5):
  print(i)
else:
  print("Sorry no i")

for i in range(6):
  print(i)
  if i == 4:
    break
i = 0
while i<7:
  print(i)
  i = i + 1

  for x in range(5):
    print("iteration no {} in for loop" .format(x+1))
  else:
    print("else block in loop")
    print("out of loop")