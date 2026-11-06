#To find the number of days in a given month (for leap year also)
def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28
year=int(input("Enter a year:"))
if year>4000 or year<1600:
    print("You have entered invalid year")
else:
    month=int(input("Enter a month:"))
    if month==2:
         print(leap_year(year))
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        print("31 days")
    elif month==4 or month==6 or month==9 or month==11:
        print("30 days")
    else:
        print("Please enter a valid month")