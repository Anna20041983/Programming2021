# Program that asks the user to input any positive integer and outputs the successive values of the following calculation
# Author: Anna Kozakiewicz

number=int(input('Please enter a positive integer:\n'))

# take the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one

def collatz(number):

    while number !=1:
        if number% 2 == 0:
            number= number//2
            print(number)

        else:
           number=  3 * number + 1
           print(number)    

collatz(number)