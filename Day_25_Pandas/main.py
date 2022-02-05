# with open("weather_data.csv", mode="r") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(type(data))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)

# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)
#

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = data["Primary Fur Color"].to_list()

gray_color = fur_colors.count("Gray")
cinnamon_color = fur_colors.count("Cinnamon")
black_color = fur_colors.count("Black")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color, cinnamon_color, black_color],
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")

