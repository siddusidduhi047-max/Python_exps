
print("Energy Conservation")

before = int(input("Enter before usage: "))
after = int(input("Enter after usage: "))

saved = before - after

print("Electricity saved:", saved)

if saved > 0:
    print("Energy saved")
else:
    print("No energy saved")
