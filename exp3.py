
print("Shopping Budget")

p1 = int(input("Enter first product price: "))
p2 = int(input("Enter second product price: "))
p3 = int(input("Enter third product price: "))
budget = int(input("Enter your budget: "))

total = p1 + p2 + p3

print("Total price:", total)

if total <= budget:
    print("Within budget")
else:
    print("Over budget")
