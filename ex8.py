import mariadb
from geopy import distance

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

def airport_types(iso):
    sql_a_type = "SELECT type, count(*) from airport "
    sql_a_type += "WHERE iso_country = '" + iso + "' GROUP BY type ORDER BY type DESC;"
    cursor = connection.cursor()
    cursor.execute(sql_a_type)
    result = cursor.fetchall()
    return result


def country_name(iso):
    sql_c_name = "SELECT DISTINCT country.name FROM airport, country "
    sql_c_name += "WHERE country.iso_country = airport.iso_country AND airport.iso_country = '" + iso + "';"
    cursor = connection.cursor()
    cursor.execute(sql_c_name)
    c_name = cursor.fetchall()
    return c_name


area_code_input = input("Enter area code: ").upper()
iso_country_name = country_name(area_code_input)
values = airport_types(area_code_input)

for tup in iso_country_name:  # Printing country name, instead of iso_code
    print(f"{tup[0]} has: ")
for ind, tuple_ in enumerate(values):  # Printing amount of each airport type
    air_type = tuple_[0]
    air_amount = tuple_[1]
    print(f"- {str(air_amount)} {air_type}")


# 3.
# Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance
# between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.

def distance_calc(airport_icao):
    sql_air_coords = "SELECT latitude_deg, longitude_deg from airport where ident = '" + airport_icao + "';"
    cursor = connection.cursor()
    cursor.execute(sql_air_coords)
    airport_coordinates = cursor.fetchall()
    return airport_coordinates


while True:
    airport1 = input("Enter ICAO code of the first airport: ").upper()
    airport2 = input("Enter ICAO code of the second airport: ").upper()
    coords_air1 = distance_calc(airport1)
    coords_air2 = distance_calc(airport2)
    if len(coords_air1) == 0 or len(coords_air2) == 0:
        print("Data not found. Please check if both of ICAO codes are correct")
        continue
    else:
        print(f"Distance between {airport1} and {airport2} is {distance.distance(coords_air1, coords_air2).km:.2f} km")
    break
