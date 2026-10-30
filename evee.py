count = int(input("Enter number of elements: ")) 
numbers = [] 
 
for i in range(count): 
    value = int(input("Enter number: ")) 
    numbers.append(value) 
 
print("Even numbers in the list are:") 
for num in numbers: 
    if num % 2 == 0: 
        print(num)
