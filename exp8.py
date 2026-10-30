
print("Examination Eligibility")

attendance = int(input("Enter attendance: "))
marks = int(input("Enter internal marks: "))

if attendance >= 75 and marks >= 40:
    print("Eligible for exam")
else:
    print("Not eligible for exam")
