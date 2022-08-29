#1

# Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit, the program instructs to release the fish
# back into the lake and notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.

min_zander_size = 42
fish_size = int(input('Enter zander size in cm: '))
if fish_size < min_zander_size:
    caught_fish_size = min_zander_size - fish_size
    print(f"Release the fish back into the lake. Caught fish is {caught_fish_size} below the size limit")
else:
    print("Great catch!")


#2

# Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description
# according to the list below.
# You must use an if/elif/else structure in your solution.
#
# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

cabin_class = input("Enter the cabin class: ").upper()

if cabin_class == "LUX":
    print("upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("windowless cabin above the car deck.")
elif cabin_class == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class")


#3

# Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
#
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.

bio_gender = input("Enter biological gender: ").lower()
hemoglobin_value = int(input("Enter hemoglobin value: "))

if bio_gender in ("f", "female"):
    if hemoglobin_value < 117:
        print("Hemoglobin value is low")
    elif 117 <= hemoglobin_value <= 155:
        print("Hemoglobin value is normal")
    elif hemoglobin_value > 155:
        print("Hemoglobin value is high")

elif bio_gender in ("m", "male"):
    if hemoglobin_value < 134:
        print("Hemoglobin value is low")
    elif 134 <= hemoglobin_value <= 167:
        print("Hemoglobin value is normal")
    elif hemoglobin_value > 167:
        print("Hemoglobin value is high")


#4

# Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.

year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0:
    print("Leap year")
elif year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")





