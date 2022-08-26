import math

# 2. Variables and interactive programs

# 1) Write a program that asks your name and then greets you by your name: Examples:
#
# If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
# If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!.

# 2) Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
#
# 3) Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.
#
# 4) Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
#
# 5) Write a program that asks the user to enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:
#
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.


# Solutions
# 1

name = input("Your name? ")
print(f"Hello, {name}!")

# 2

circle_radius = int(input("Enter radius: "))
print(f"The circle area is: {float(math.pi * pow(circle_radius, 2)):.2f}")

# 3

rectangle_length = float(input("Enter length: "))
rectangle_width = float(input("Enter width: "))
print(f"The perimeter of the rectangle is: {round(rectangle_width + rectangle_length, 2)}")
print(f"The area of the rectangle is: {round(rectangle_width * rectangle_length, 2)}")

# 4

num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))
num_3 = int(input("Enter number 3: "))

print(f"The sum of 3 given numbers is: {num_1 + num_2 + num_3}")
print(f"The product of 3 given numbers is: {num_1 * num_2 * num_3}")
print(f"The average of 3 given numbers is: {round(float((num_1 + num_2 + num_3) / 3), 2)}")


#5

entered_talents = float(input("Enter talents: "))
entered_pounds = float(input("Enter pounds:  "))
entered_lots = float(input("Enter lots: "))

lot = 13.3
pound = 32 * lot
talent = 20 * pound

entered_weight_in_g = entered_talents * talent + entered_pounds * pound + entered_lots * lot
entered_weight_in_kg = entered_weight_in_g / 1000
weight_in_g_left = (float(entered_weight_in_kg - int(entered_weight_in_kg)) * 1000)
print(f"The weight in modern units: {int(entered_weight_in_kg)} kilograms and {weight_in_g_left:.2f} grams")







