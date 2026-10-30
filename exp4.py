
print("Student Performance")

mark1 = int(input("Enter first exam marks: "))
mark2 = int(input("Enter second exam marks: "))

difference = mark2 - mark1

print("Change in marks:", difference)

if difference > 0:
    print("Marks improved")
elif difference < 0:
    print("Marks decreased")
else:
    print("Marks remained the same")
