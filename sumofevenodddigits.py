num = int(input("Enter a number: "))
digit = num % 10

while num!=0:
    digit1 = num % 10
    num = num // 10
print("FIRST DIGIT",digit1)
print("LAST DIGIT",digit)
#CAN ALSO USE WITH REVERSE AND LARGEST LOGIC
