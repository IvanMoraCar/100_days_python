# with open("C:\\Projects\\100_days\\Files\\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
#
# with open("C:\\Projects\\100_days\\Files\\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#         print(row)
#     print(temperatures)

import pandas

data = pandas.read_csv("C:\\Projects\\100_days\\Files\\weather_data.csv")

dic_panda = data.to_dict()
# print(type(data))
# print(data["temp"])
# print(dic_panda)
#
# sum_temp = sum(data["temp"]) / len(data["temp"])
# print(sum_temp)

# temp_list = data["temp"].to_list()
# avr_temp = sum(temp_list) / len(temp_list)
# print(round(avr_temp))
print(data["temp"].mean())
print(data["temp"].max())

#Get the data in Columns
print(data["condition"])
print(data.condition)

#
