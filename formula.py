import math

def square_footage():
    width = input("Please enter the width of the house: ")
    length = input("Please enter the length of the house: ")
    return f"The square footage of your house is {int(length) * int(width)}"

def circum():
    r = input("Enter the radius of the circle: ")
    return 2 * math.pi * int(r)