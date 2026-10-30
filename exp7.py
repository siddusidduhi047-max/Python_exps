
print("Traffic Flow Analysis")

vehicles = int(input("Enter number of vehicles: "))

if vehicles < 50:
    print("Low traffic")
elif vehicles < 100:
    print("Medium traffic")
else:
    print("High traffic")
