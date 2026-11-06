"""Calculate BMI and display a basic adult BMI category."""

try:
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    if weight <= 0 or height <= 0:
        print("Weight and height must both be greater than zero.")
    else:
        bmi = weight / (height ** 2)
        print(f"Your BMI is {bmi:.2f}")
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal range"
        elif bmi < 30:
            category = "Overweight"
        elif bmi < 35:
            category = "Obese"
        else:
            category = "Clinically obese"
        print(f"Your BMI category is: {category}")
except ValueError:
    print("Invalid input. Enter numbers for weight and height.")