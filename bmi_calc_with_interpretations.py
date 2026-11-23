
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal")
else:
    print ("overweight")
