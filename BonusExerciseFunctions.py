# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     grades_list = {}
#     grades_list["max"] = max(grades)
#     grades_list["min"] = min(grades)
#     return grades_list
#
#
# grades_list = get_max()
# for grade in grades_list.values():
#     print(grade)

# def get_maximum():
#     celsius_local = [14, 15.1, 12.3]
#     maximum = max(celsius_local)
#     print(maximum)
#     return maximum
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
# print(fahrenheit)
#
# def get_temperature_average():
#     with open("files/data.txt", "r") as file:
#         data = file.readlines()
#     try:
#         data = [float(temp) for temp in data[1:]]
#     except ValueError:
#         print("Error, not a number.")
#     print(data)
#     average_temp = sum(data) / len(data)
#     return average_temp
#
#
# temperature_average = get_temperature_average()
# print(temperature_average)
# #


# def speed(travel_data_local):
#     return travel_data_local["distance"] / travel_data_local["time"]
#
#
# travel_data = {}
# travel_data["distance"] = float(input("Enter the distance: "))
# travel_data["time"] = float(input("Enter the time: "))
#
# travel_data["speed"] = speed(travel_data)
# print(f"The travel speed was {travel_data['speed']}")
#
#
# def check_password(password_local):
#     password_check = {"upper": False, "lower": False, "length": False, "digit": False}
#     if len(password_local) >= 8:
#         password_check["length"] = True
#     for char in password_local:
#         if char.isupper():
#             password_check["upper"] = True
#         if char.islower():
#             password_check["lower"] = True
#         if char.isdigit():
#             password_check["digit"] = True
#     return all(password_check.values())
#
#
# password = input("Enter your password: ")
#
# is_password_strong = check_password(password)
# if is_password_strong:
#     print("The password is strong.")
# else:
#     print("The password is weak.")

# text = """
# Principles of productivity:
# Managing your inflow.
# Systemizing everything that repeats.
# """
#
# print(text)
# def end_program(error_message):
#     exit(error_message)
#     return None
#
#
# def calculate_age(year_of_birth, year_current = 2022):
#     return year_current - year_of_birth
# birth_year = ""
# year = ""
# age = 0
# try:
#     birth_year = input("Please enter the year of your birth: ")
#     birth_year = float(birth_year)
# except ValueError:
#     end_program("Error, invalid entry.")
#
# try:
#     year = input("Please enter a year: ")
#     if year.strip() == "":
#         age = calculate_age(birth_year)
#     else:
#         year = float(year)
#         age = calculate_age(birth_year, year)
# except ValueError:
#     end_program("Error, invalid entry.")
# if age > 120:
#     print("Wow. You are old.")
# else:
#     print(f"You are {age} years old.")

# def get_name_list(names_local):
#     return names.split(",")
#
#
# names = input("Please enter a list of names separated by commas: ")
# names_list = get_name_list(names)
# print(names_list)

# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
#
#
# time = calculate_time(100)
# print(time)

# from bonus_functions import *
#
# measure_imperial = input("Enter the length in feet and inches: ")
# try:
#     measure_list = parse_feet_inches(measure_imperial)
#     measure_list = convert_list_to_float(measure_list)
#     measure_dict = convert_list_to_dict(measure_list)
#     meters_feet = feet_to_meters(measure_dict["feet"])
#     meters_inch = inches_to_meters(measure_dict["inches"])
#     print(f"The total measurement in meters is {meters_inch + meters_feet:.2f} meters.")
# except ValueError:
#     why("There has been a Value Error.")
# except IndexError:
#     why("There has been an Index Error.")

# import bonus_functions
#
# try:
#     temp = input("Please enter the temperature of the water: ")
#     temp = float(temp)
#     state = bonus_functions.is_freezing(temp=temp)
#     print(f"The state of the water is {state}.")
# except ValueError:
#     bonus_functions.why("Error, please enter a temperature.")

import time
from bonus_functions import count_period

statement = input("Please enter a statement: ")
nr_of_periods = count_period(statement=statement)
print(f"There are {nr_of_periods} periods in the statement, \"{statement}\"")


