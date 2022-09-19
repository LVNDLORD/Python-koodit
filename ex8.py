import mariadb

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Bosch16v',
    autocommit=True
)


# 1. Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the
# corresponding airport name and location (town) from the airport database used on this course. The ICAO codes are
# stored in the ident column of the airport table.


def airport_name_and_location(icao):
    sql = "SELECT name, municipality FROM airport WHERE airport.ident = '" + icao + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return


user_input = input("Enter ICAO code of the airport: ").upper()
airport_name_and_location(user_input)


# 2.Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in
# that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.

#   returning type and count

#   SELECT airport.type, count(*) from airport
#   where airport.iso_country = 'FI' group by type order by type desc;

# working but with iso_country only, not with country name

def airport_types(iso):
    sql_a_type = "SELECT type, count(*) from airport "
    sql_a_type += "WHERE iso_country = '" + iso + "' GROUP BY type ORDER BY type DESC;"
    cursor = connection.cursor()
    cursor.execute(sql_a_type)
    result = cursor.fetchall()
    print(result)
    return


area_code_input = input("Enter area code: ").upper()
airport_types(area_code_input)

# values = [('small_airport', 65), ('medium_airport', 30), ('large_airport', 1), ('heliport', 15), ('closed', 6)] # - [list(tuples)]
# values_a_types = airport_types()
# print(f"values a types {values_a_types}")

###################

#   returning country name, type and count
#   SELECT distinct country.name, airport.type, count(*) from airport, country
#   where country.iso_country = airport.iso_country and airport.iso_country = 'FI'
#   group by type order by type desc;
###
# def airport_types(iso):
#     sql_a_type = "SELECT type, count(*) from airport "
#     sql_a_type += "WHERE iso_country = '" + iso + "' GROUP BY type ORDER BY type DESC;"
#     sql_country_name = "SELECT DISTINCT country.name FROM country, airport "
#     sql_country_name += "WHERE country.iso_country = airport.iso_country AND airport.iso_country = '" + iso + "';"
#     cursor = connection.cursor()
#     cursor.execute(sql_a_type, sql_country_name)
#     result = cursor.fetchall()
#     print(result)
#     print(type(result))
#     return
#
# area_code_input = input("Enter area code: ").upper()
# airport_types(area_code_input)
###






# SELECT distinct country.name, airport.type, count(*) from airport, country
# where country.iso_country = airport.iso_country and airport.iso_country = 'FI'
# group by type order by type desc;


# 3.
# data received as set, or dictionary, write f"" and target indexes

# Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance
# between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the library by
# selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the
# installation.

input()
input()

# fetch coordinates (x, y) - (x, y)
# pip install geopy
