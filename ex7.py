import string

# 1. Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.

seasons = ("spring", "summer", "autumn", "winter")
input_num = int(input("Enter the number of the month: "))
if input_num in {12, 1, 2}:
    print(seasons[3])
elif input_num in {9, 10, 11}:
    print(seasons[2])
elif input_num in {6, 7, 8}:
    print(seasons[1])
elif input_num in {3, 4, 5}:
    print(seasons[0])
else:
    print("Input number should be only in range 1-12")

# 2. Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending on whether
# the name was entered for the first time. Finally, the program lists out the input names one by one,
# one below another in any order. Use the set data structure to store the names.

names = set()

while True:
    input_data = input("Enter a name: ")
    if input_data == "":
        print(names)
        break
    elif input_data in names:
        print("Existing name")
    else:
        print("New name")
        names.add(input_data)


# 3. Write a program for fetching and storing airport data. The program asks the user if they want to
# enter a new airport, fetch the information of an existing airport or quit.
#
# If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints
# out the corresponding name.
# If the user chooses to quit, the program execution ends. The user can choose a new option as many times they
# want until they choose to quit.
#
# (The ICAO code is an identifier that is unique to each airport.
# For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different
# airports online.)

airports = {"LTAI": "Antalya Airport", "EHAM": "Amsterdam Schiphol Airport"}

while True:
    options = int(input("1 - enter a new airport\n2 - fetch airport information\n3 - quit\n"))
    if options not in {1, 2, 3}:
        print("Please choose between options 1-3")
        continue
    if options == 3:
        break
    elif options == 1:
        entered_ICAO = input("Enter airport ICAO: ").upper()
        entered_name = string.capwords(input("Enter airport name: "))
        airports[entered_ICAO] = entered_name
    elif options == 2:
        searched_ICAO = input("Enter searched airport ICAO: ").upper()
        if searched_ICAO in airports:
            print(airports.get(searched_ICAO))

print(airports)
