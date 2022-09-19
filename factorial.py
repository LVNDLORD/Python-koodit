# calc the factorial of a given num

# num_given = int(input('Enter a number: '))
# factorial = 1
#
# while num_given >= 1:
#     factorial = factorial * num_given
#     num_given - 1
#     print(f"factorial of {num_given} is {factorial}")

number = int(input("Type a number: "))
factorial = number
if number <= 0:
    print("Thanks and bye!")
else:
    for i in range(1, number):
        factorial = factorial * i
    print(f"The factorial of {number} is {factorial}")
