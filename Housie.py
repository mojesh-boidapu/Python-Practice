import random
print("Welcome to Housie")
numbers = list(range(1, 91))
random.shuffle(numbers)
for number in numbers:
    command=input("Press Enter (or 'q' to quit):")
    if command == "q":
        print("Housie stopped.")
        break
    print("Number:", number)