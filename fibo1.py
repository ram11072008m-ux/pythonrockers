number1 = int(input("Enter first number: ")) 
number2 = int(input("Enter second number: ")) 
 
addition = lambda a, b: a + b 
subtraction = lambda a, b: a - b 
multiplication = lambda a, b: a * b 
division = lambda a, b: a / b 
 
print("Addition result is:", addition(number1, number2)) 
print("Subtraction result is:", subtraction(number1, number2)) 
print("Multiplication result is:", multiplication(number1, 
number2)) 
print("Division result is:", division(number1, number2))
