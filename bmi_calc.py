weight = float(input("How many kiograms do you weigh?: "))
height = float(input("How tall are you in metres?: "))
bmi = weight / (height * height)
bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"You are underweight. Your BMI is {bmi}")
elif bmi < 24.9:
    print(f"You have a normal weight. Your BMI is {bmi}")
elif bmi < 29.9:
    print(f"You are overweight. Your BMI is {bmi}")
elif bmi >= 30:
    print(f"You are obese. Your BMI is {bmi}")
