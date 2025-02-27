import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))       #<class 'pandas.core.frame.DataFrame'>
print(f"Prints the entire data \n{data}\n")

print(f"Print the part of the data ie only temp row which is series \n{data['temp']}\n")
print(type(data['temp']))       #<class 'pandas.core.series.Series'>

print(f"Convert the data to list \n {data['temp'].to_list()}\n")     #this will convert the temperature of data to list


data_dict = data.to_dict()
print(f"Converts the data to dictionary \n{data_dict}\n")
print(type(data_dict))      #<class 'dict'>

temp_list = data['temp'].to_list()
avg = sum(temp_list) /len(temp_list)
print(f"Prints the avg temp of the list ie {avg}\n or")

print(f"Using mean func we get the same avg temp {data['temp'].mean()}")

print(data['temp'].max())

print(f"We can either call with method like .temp or function like ['temp'] as \n{data.temp}\n")

print(f"If we want o pull only the Monday row we can do as so \n"
      f"{data[data.day == 'Monday']}\n")

print(f"Print the data which is having the maximum temp from the data\n{data[data.temp == data.temp.max()]}\n")

print("Converting the temp from c to f ")
Monday_temp = data[data.day == 'Monday']
Monday_temp_f =(Monday_temp.temp * 9/5) + 32
print(Monday_temp_f)

print("\n########## Create the data frame from scratch   ############")
data_dict = {
    "name": ["savithri", "gayathri", "triveni"],
    "age": [23, 24, 32]
}

data = (pandas.DataFrame(data_dict))
print(f"This will convert the dictionary data to nice table format using panda \n{data}\n")

print(f"This will convert the data dictionary to csv using csv\n{data.to_csv()}\n")