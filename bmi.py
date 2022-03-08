# Calculate BMI
# Author: Anna Kozakiewicz

# we must calculate bmi by dividing height by weight

height = int(input("Please enter your height in cm: "))
weight = int(input("Please enter your weight in kg: "))
BMI = weight/(height/100)**2

print(f"You BMI is {BMI}")
