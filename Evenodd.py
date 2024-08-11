numbers = (input("Enter a numbers")).split()
list = [int(i) for i in numbers]
even = [num for num in list if num % 2 == 0]
odd = [num for num in list if num % 2 != 0]

print("Even numbers:", even)
print("Odd numbers:", odd)
