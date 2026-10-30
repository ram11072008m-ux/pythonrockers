print("MENU :\n1.PIZZA\t\tRS:200\n2.BURGER\tRS:120\n3.PASTA\t\tRS:150\n4.SANDWITCH\tRS:100")
order=int(input("ENTER YOUR ORDER NUMBER:"))
match order:
    case 1:
        print("you ordered PIZZA")
        print("PRICE=RS:200")
    case 2:
        print("you ordered BURGER")
        print("PRICE=RS:120")
    case 3:
        print("you ordered PASTA")
        print("PRICE=RS:150")
    case 4:
        print("you ordered SANDWITCH")
        print("PRICE=RS:100")
    case _:
        print("INVALID ORDER")
        
