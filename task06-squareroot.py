# Function to return square root of a number using Newtons Method
# Author: Anna Kozakiewicz

def NewtonMethod (number, number_items=100):
    num = float (number)
    for i in range (number_items):
        number = 0.5 * (number + num / number)
    return number

num = float(input ("Please enter a positive number : "))

print ("Square root of", num, "is approx : ", NewtonMethod (num))
