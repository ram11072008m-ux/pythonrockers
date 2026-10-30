n=int(input("ENTER THE NUMBER:"))
n1=0
n2=0
for i in range(1,n+1):
    if i%2==0:
        n1+=1
    else:
        n2+=1
   
print("the count of odd:",n2)
print("the count of even:",n1)
