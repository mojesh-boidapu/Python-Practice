#leap year or not
year=int(input("enter year:"))
if year>=1600 and year<=4000:
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("Given year is a 'leap year'")
            else:
                print("Given year is not a leap year")
        else:
            print("Given year is a 'leap year'")
    else:
        print("Given year is not a leap year")
else:
    print("Give a valid year")