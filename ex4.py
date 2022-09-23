import random

# 1

# Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

i = 1
while i < 1000:
    if i % 3 == 0:
        print(i)
    i += 1


# 2

# Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

inch = 2.54

while True:
    value = float(input("Inch input: "))
    if value >= 0:
        result_in_cm = value * inch
        print(f"{result_in_cm:.2f} cm")
    else:
        break


# 3

# Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.

smallest = None
largest = None

while True:
    num = input("Enter a number: ")
    if len(num) > 0:
        num = int(num)
        if largest is None:
            largest = num
        elif largest < num:
            largest = num

        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num
    elif num == "":
        print(f"smallest: {smallest}, largest: {largest}")
        break


# 4

# Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.

random_num = random.randint(1, 10)

while True:
    user_input = int(input("Enter number: "))
    if user_input == random_num:
        print("Correct")
        break
    elif user_input < random_num:
        print("Too low")
    elif user_input > random_num:
        print("Too high")


# 5

# Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome. After five failed attempts the program prints out
# "Access denied".
# The correct username is python and password rules.

j = 0
username = "python"
password = "rules"

while j < 5:
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    j += 1
    if input_username == username and input_password == password:
        print("Welcome")
        break
    elif input_username != username or input_password != password:
        if j == 5:
            print("Access denied")
            break
        else:
            continue


# 6

# Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit circle.
# A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B is drawn around
# the unit circle so that circle A is completely inside the square. The corners of the square are now
# (-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square,
# the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A compared
# to the area of square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method for calculating an approximation
# of the value of pi: Let's generate a large number of random points, such as one million, inside square B.
# Let N be the total number of random points. Each point inside the square is tested for whether it resides inside
# circle A. Let n be the total number of points that fall inside circle A. Now we have n/N≈π/4,
# and from that we get π≈4n/N.
# Write a program that asks the user how many random points to generate, and then calculates the approximate value of pi
# using the method explained above. At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).

# gen random x, y points
# check if < 1    x^2+y^2<1
    # if yes - circle, no - square
# π≈4n/N

number_of_points = int(input("How many random points to generate? "))
circle_points = 0
square_points = 0
approximation_of_pi = None

for k in range(number_of_points):
    random_x = random.uniform(-1, 1)
    random_y = random.uniform(-1, 1)

    distance_from_origin = pow(random_x, 2) + pow(random_y, 2)

    if distance_from_origin < 1:
        circle_points += 1
    square_points += 1
    approximation_of_pi = 4 * circle_points / square_points

print(circle_points)
print(square_points)
print(f"Approximation of Pi: {approximation_of_pi}")
