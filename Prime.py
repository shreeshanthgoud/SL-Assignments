n=int(input("Enter a  number:"))
def prime_number_check(num1):
    is_prime = True
    if n==0 or n==1:
        is_prime = False
    for i in range(2,n):
        if n%i==0:
            is_prime = False
    if is_prime == True:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
prime_number_check(n)