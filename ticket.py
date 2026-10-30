age = int(input("Enter age: "))
timing = input("Enter show timing: ")

if age < 12:
    price = 100

    if timing == "morning":
        price = price - 20

    print("Child Ticket")
    print("Ticket Price:", price)

elif age <= 59 and age >=12 :
    price = 200

    if timing == "morning":
        price = price - 20

    print("Adult Ticket")
    print("Ticket Price:", price)

else:
    price = 120

    if timing == "morning":
        price = price - 20

    print("Senior Citizen Ticket")
    print("Ticket Price:", price)
