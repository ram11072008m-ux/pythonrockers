salary = int(input("Enter salary: "))
exp = int(input("Enter years of experience: "))

if exp >= 5:
    bonus = salary * 10 / 100
    print("Bonus:", bonus)
    print("Total Salary:", salary + bonus)

elif exp >= 2:
    bonus = salary * 5 / 100
    print("Bonus:", bonus)
    print("Total Salary:", salary + bonus)

else:
    print("No bonus")
    print("Total Salary:", salary)
