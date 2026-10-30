
print("Branch Expense Analysis")

branch1 = [1000, 2000, 1500]
branch2 = [2500, 3000, 2000]

total1 = sum(branch1)
total2 = sum(branch2)

print("Branch 1 total:", total1)
print("Branch 2 total:", total2)

print("Branch 1 average:", total1 / 3)
print("Branch 2 average:", total2 / 3)

if total1 > total2:
    print("Branch 1 has higher expenses")
elif total2 > total1:
    print("Branch 2 has higher expenses")
else:
    print("Both branches have equal expenses")
