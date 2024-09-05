import pandas
data = pandas.read_csv("C:\\Projects\\100_days\\Files\\weather_data.csv")
print(type(data))
#print(data["temp"])

data_dict = data.to_dict()

# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# temp_count_days = len(temp_list)
# temperature_prom = 0
#
# for v in temp_list:
#     temperature_prom += v
#
# print(round(temperature_prom / temp_count_days))

# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get data in Colums
# print(data.condition)
# print(data["condition"])
#
# #Get Data in row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data["temp"].max()])
#
monday = data[data.day == "Monday"]
monday_temp = monday.temp