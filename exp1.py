
print("Manufacturing Cost")

material = int(input("Enter material cost: "))
labour = int(input("Enter labour cost: "))
machine = int(input("Enter machine cost: "))
selling = int(input("Enter selling price: "))

cost = material + labour + machine
profit = selling - cost

print("Total cost:", cost)
print("Profit:", profit)

if profit > 0:
    print("Profit achieved")
else:
    print("No profit")
