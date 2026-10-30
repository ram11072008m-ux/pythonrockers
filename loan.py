age = int(input("Enter age: "))
salary = int(input("Enter salary: "))
creditscore = int(input("Enter credit score: "))
employment = input("Enter employment status: ")

if age >= 21 and age <= 60:

    if salary >= 25000:

        if creditscore >= 700:

            if employment == "employed":
                print("Loan Approved")

            else:
                print("Loan Rejected: Applicant must be employed")

        else:
            print("Loan Rejected: Credit score must be 700 or above")

    else:
        print("Loan Rejected: Salary must be ₹25,000 or above")

else:
    print("Loan Rejected: Age must be between 21 and 60")
