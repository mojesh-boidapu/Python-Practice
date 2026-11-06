#Rollercoaster Ticket
height=float(input("Enter height in feet: "))
age = int(input("What is your age ?\n"))
bill=0
if height < 0 or age <= 0:
    print("Height and age can't be negative")
elif 3 <= height < 8 and 8 <age <= 55:
    print("You can ride the Rollercoaster")
    if age<=12:
        bill=100
        print(f"Ticket price is {bill} Rs")
    elif age<=18:
        bill=150
        print(f"Ticket price is {bill} Rs")
    else:
        bill=250
        print(f"Ticket price is {bill} Rs")
    photo=input("Do you want any photos?. for photos it is extra 50 Rs (Y/N):")
    if photo=="n" or photo=="N":
        print(f"Ok then your bill is {bill} ")
    elif photo=="y" or photo=="Y":
        print(f"Your bill is {bill+50}")
    else:
        print("Enter valid input")
else:
    print("You can't ride the Rollercoaster")
print("Enjoy the ride")