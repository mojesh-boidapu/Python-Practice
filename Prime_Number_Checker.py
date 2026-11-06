#Prime number or not using functions
def prime_checker(number):
    is_prime=True
    if number==1:
        print("Given number is not a prime number")
    else:
        for i in range(2,number):
            if number%i==0:
                is_prime=False
        if is_prime==True:
            print("Given number is a prime number")
        else:
            print("Given number is not a prime number")

n = int(input("Enter a number:"))
prime_checker(number=n)
