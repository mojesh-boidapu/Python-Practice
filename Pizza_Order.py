#pizza order program
size=input("What size of pizza do you want Small/Medium/Large(S/M/L)?")
bill=0
if size=='S' or size=='s':
    bill+=100
    print(f"Your small pizza price is {bill} Rs")
elif size=='M' or size=='m':
    bill+=200
    print(f"Your Medium pizza price is {bill} Rs")
else:
    bill+=300
    print(f"Your large pizza price is {bill} Rs")
add_pepperoni=input("Do you want to add pepperoni?(Y/N)")
if add_pepperoni=='Y' or add_pepperoni=='y':
    if size=='S' or size=='s':
        bill+=30
        print(f"Your pepperoni pizza bill will be {bill} Rs ")
    elif size=='M' or size=='m' or size=='L' or size=='l':
        bill+=50
        print(f"Your pepperoni pizza bill will be {bill} Rs ")
extra_cheese=input("Do you want to add any extra cheese?(Y/N)")
if extra_cheese=='Y' or extra_cheese=='y':
    bill+=20
    print(f"Your extra cheese pizza bill will be {bill} Rs ")
else:
    print(f"Your total bill will be Rs{bill}")
    print(f"Enjoy the pizza")