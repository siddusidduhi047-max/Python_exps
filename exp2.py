
print("Travel Budget")

hotel = int(input("Enter hotel expense: "))
food = int(input("Enter food expense: "))
transport = int(input("Enter transport expense: "))

rate = int(input("Enter exchange rate: "))
budget = int(input("Enter budget in rupees: "))

total = (hotel + food + transport) * rate

print("Total expense in rupees:", total)

if total <= budget:
    print("Within budget")
else:
    print("Over budget")
