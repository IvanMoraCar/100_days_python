import pandas
data = pandas.read_csv("C:\\Projects\\100_days\\Files\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(type(data))
# #print(data["temp"])
#
# #data_dict = data.to_dict()
#
# # print(data_dict)
# #
#
# # print(temp_list)
#
# # temp_count_days = len(temp_list)
# # temperature_prom = 0
# #
# # for v in temp_list:
# #     temperature_prom += v
# #
# # print(round(temperature_prom / temp_count_days))
#
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # #Get data in Colums
# # print(data.condition)
# # print(data["condition"])
# #
# # #Get Data in row
# # print(data[data.day == "Monday"])
# #
# # print(data[data.temp == data["temp"].max()])
# #
# #monday = data[data.day == "Monday"]
# #monday_temp = monday.temp
#
#
# day_max_temp = data[data.temp == data.temp.max()]
# print(day_max_temp)
# print(day_max_temp.temp * 9 / 5 + 32)
#
# #Create a new file cvs
#
# data_dict = {
#
#     "studenys" : ["Amy", "James", "Angela"],
#     "cores": [76, 56, 65]
#
# }
#
# data = pandas.DataFrame(data_dict)
#
# data.to_csv("C:\\Projects\\100_days\\Files\\new_data.csv")
# fur_color = data["Primary Fur Color"]
#
# fur_color_list = fur_color.to_list()
#
# colors_dict = {
#     "Fur Color": ["gray", "red", "black"],
#     "Count": [0, 0, 0]
# }
#
# for color in fur_color_list:
#         if color == "Cinnamon":
#             colors_dict["Count"][1] += 1  # Incrementa el contador para "red"
#         elif color == "Gray":
#             colors_dict["Count"][0] += 1  # Incrementa el contador para "gray"
#         elif color == "Black":
#             colors_dict["Count"][2] += 1  # Incrementa el contador para "black"


grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

colors_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]

}

data = pandas.DataFrame(colors_dict)
data.to_csv("C:\\Projects\\100_days\\Files\\squirrel_count2.csv")

|