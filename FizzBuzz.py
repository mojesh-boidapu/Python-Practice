#FizzBuzz program
try:
    n_number = int(input("Enter the last number: "))
    if n_number < 1:
        print("Please enter a positive integer greater than 0.")
    else:
        for number in range(1, n_number + 1):
            if number % 3 == 0 and number % 5 == 0:
                print("FizzBuzz")
            elif number % 3 == 0:
                print("Fizz")
            elif number % 5 == 0:
                print("Buzz")
            else:
                print(number)
except ValueError:
    print("Invalid input. Please enter a whole number.")
