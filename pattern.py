for i in range(6):
    for j in range(6):
        if i==0 and i==i-1:
            if j==0 and j==j-1: 
                print("*",end="  ")
            else:
                print()
    print()
