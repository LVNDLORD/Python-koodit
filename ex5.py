import random

# 1. Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the
# sum of the numbers. Use a for loop.

dice_amount = int(input("How many dice to roll?: "))
dice_sum = 0

for roll in range(dice_amount):
    dice_range = random.randint(1, 6)
    dice_sum += dice_range
print(dice_sum)

# 2. Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

num_list = []
while True:
    num_entered = input("Enter a number: ")
    if num_entered == "":
        num_list.sort(reverse=True)
        print(num_list[:5])
        break
    else:
        num_list.append(int(num_entered))

# 3. Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
# For example, number 13 is a prime number as can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, number 21 for example is not a prime number as it can be also be divided by numbers 3 and 7.

num = int(input("Enter number: "))
if num > 1:
    for i in range(2, num):
        # print(i)
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# 4. Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the
# names) and stores them into a list structure. Finally, the program prints out the names of the cities one by one,
# one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop
# to iterate through the list.

cities = []
for city in range(5):
    cities.insert(0, input("Enter city name: "))
cities2 = cities.copy()
for item in cities:
    print(cities2.pop())
