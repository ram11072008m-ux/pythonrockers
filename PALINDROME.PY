n=int(input("ENTER A VALUE:"))
n1=n
s=0
while(n):
    k=n%10
    s=(s*10)+k
    n=n//10
if n1==s:
    print("THE GIVEN VALUE IS PALINDROME",n1)
else:
    print("THE GIVEN VALUE IS NOT A PALINDROME",n1)
