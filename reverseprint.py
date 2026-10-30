num=int(input("enter a number:"))
rev=0
while num!=0:
    r=n%10
    rev=(rev*10)+r
    num//=10
print(rev)
