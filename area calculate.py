print("1. Circle\n 2. Rectangle\n 3. Square\n 4. Triangle")

choice = int(input("Enter your choice: "))

match choice:

    case 1:
        radius = int(input("Enter radius: "))
        area = 3.14 * radius * radius
        print("Area of Circle:", area)

    case 2:
        length = int(input("Enter length: "))
        breadth = int(input("Enter breadth: "))
        area = length * breadth
        print("Area of Rectangle:", area)

    case 3:
        side = int(input("Enter side: "))
        area = side * side
        print("Area of Square:", area)

    case 4:
        base = int(input("Enter base: "))
        height = int(input("Enter height: "))
        area = 0.5 * base * height
        print("Area of Triangle:", area)

    case _:
        print("Invalid choice")
