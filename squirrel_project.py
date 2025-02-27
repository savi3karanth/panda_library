import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(black_squirrel_count)
print(red_squirrel_count)

#to print the data in dictionary format
data_dict = {
    "squirrel color": ["Grey", "Cinnamon", "Black"],
    "count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count],
}
print(data_dict)

# we can convert the above to data frame
data_dict_to_dataframe = pandas.DataFrame(data_dict)
print(data_dict_to_dataframe)

#to covert the data frame to csv and give a new file name
data_dict_to_dataframe.to_csv("squirrel_count.csv")
