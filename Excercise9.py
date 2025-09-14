# Ask the user for temperature in Celsius. If > 30 → "Hot", if between 15–30 → "Moderate", else "Cold"
a = int(input("Enter today Temperature in Celsius: "))
if (a == 30):
    print("Today's Temperature is very hot")
elif 15 <= a <= 30:
    print("Today's Temperature is Moderate")
else:
    print("Today's Temperature is cold freezing")
