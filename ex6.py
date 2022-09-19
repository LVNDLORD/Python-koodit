# 1. Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6. The main program should print out the result of
# each roll.

import random


def ran():
    random_num = random.randint(1, 6)
    return random_num


while True:
    dice = ran()
    print(dice)
    if dice == 6:
        break

# 2.Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in the main program continues until
# the program gets the maximum number on the dice, which is asked from the user at the beginning.

user_input = int(input("Enter number of sides: "))
i = 1


def rand(y):
    random_num = random.randint(1, y)
    return random_num


while True:
    dice = rand(user_input)
    print(f"roll num {i} value : {dice}")
    i += 1
    if dice == user_input:
        break

# 3. Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

gallon = 3.78


def gas(y):
    gas_in_liters = y * gallon
    return gas_in_liters


while True:
    gas_in_gallons = int(input("Enter volume in gallons: "))
    if gas_in_gallons < 0:
        break
    print(f"Volume in liters {gas(gas_in_gallons)}")


# 4. Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list, call the function, and print out the value it returned.

integers = [1, 2, 3, 4, 5, 6]


def sum_function(y):
    summary = 0
    for j in y:
        summary += j
        # print(i)
    return summary


print(sum_function(integers))


# 5. Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original list
# except that all uneven numbers have been removed.
# For testing, write a main program where you create a list, call the function,
# and then print out both the original as well as the cut-down list.

def uneven(y):
    uneven_list = []
    for k in y:
        if k % 2 != 0:
            uneven_list.append(k)
    return uneven_list
#   return uneven_list, y    # for testing


print(integers)
print(uneven(integers))


# 6. Write a function that receives two parameters: the diameter of a round pizza in centimeters
# and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides
# better value for money (which of them has a lower unit price). You must use the function you wrote
# for calculating the unit prices.

f = 1
first = 0


def pizza(x, y):
    price_per_square_meter = round(y / ((float(x) / (100 * 2)) ** 2), 2)  # calc the area in sq meter
    return price_per_square_meter


while f <= 2:
    pizza_diameter = int(input(f"Please enter the diameter of pizza {f}: "))
    pizza_price = int(input(f"Please enter the price of pizza {f}: "))
    pizza_value = pizza(pizza_diameter, pizza_price)
    f += 1
    if first == 0:
        first = pizza_value
        continue
    else:
        if pizza_value < first:
            print(f"pizza 2 has better value with {pizza_value}€ per square meter")
        elif pizza_value == first:
            print(f"Both pizzas have the same value of {pizza_value}€ per square meter")
        else:
            print(f"Pizza 1 has a better value with {first}€ per square meter")
