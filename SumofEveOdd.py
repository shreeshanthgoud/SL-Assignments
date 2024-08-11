numbers = input("Enter numbers separated by spaces: ").split()
list = [int(i) for i in numbers]

even = [ num for num in list if num % 2 == 0]
odd = [ num for num in list if num % 2 != 0]

sum_even = sum(even)
sum_odd = sum(odd)

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
