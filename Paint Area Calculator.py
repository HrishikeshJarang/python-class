#Paint Area Calculator

import math

def paint_calc(height, width, cover):
    number_of_cans = ((height * width) / cover)
    round_up_cans = math.ceil(number_of_cans)  # ceil = ceiling of the number - means rounding up number
    print(f"You'll need {round_up_cans} cans of paint")

test_h = int(input("Enter the height of the wall in meters: "))  # Height of wall in "m"
test_w = int(input("Enter the width of the wall in meters: "))   # Width of wall in "m"
coverage = 5  # Coverage per can of paint in square meters

paint_calc(height=test_h, width=test_w, cover=coverage)

