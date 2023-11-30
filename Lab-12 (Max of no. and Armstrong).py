#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     30-11-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def max_of_three(a, b, c):
    """Return the largest of three numbers."""
    return max(a, b, c)

def is_armstrong(number):
    """Check if a number is an Armstrong number."""
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    return armstrong_sum == number

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = max_of_three(num1, num2, num3)
print(f"The largest of {num1}, {num2}, and {num3} is: {largest}")

num = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

