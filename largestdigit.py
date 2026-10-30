num = int(input("Enter a number: "))

lar = 0

while num > 0:
    digit = num % 10

    if digit > lar:
        lar = digit

    num = num // 10

print("Largest digit is:", lar)
