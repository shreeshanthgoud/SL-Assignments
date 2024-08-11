n = int(input("Enter the number:"))
sum = 0
while n!=0:
    dig = n%10
    sum+= dig
    n = n//10
print("The Sum of the digits is ",sum)