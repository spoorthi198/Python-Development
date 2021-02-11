import csv

# with open("weather_data.csv",'r') as data:
#     contents =data.readlines()

# with open("weather_data.csv",'r') as data_file:
#     data=csv.reader(data_file)
#     temperature= []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv('weather_data.csv')
print(type(data['temp']))

data_file = data.to_dict()
print(data_file)

data_list = data["temp"].to_list()
# temp = 0
# for x in data_list:
#     temp += x
# print(temp)
#
# avg_temp = temp/len(data_list)


avg_temp= data["temp"].mean()
print(f"Avg_temp is :  {avg_temp} ")

max_temp = data["temp"].max()
print(f" max temp is : {max_temp}")

# fetch the row
print(data[data.temp == max_temp])

# monday = data[data.day == 'monday']
# monday_temp = int(monday.temp)
# monday_temp_f = (monday_temp * 9/5) + 32
#
# print(monday_temp_f)


# creating dataframe from scratch

data_dict = {
    "students" : ['spoorthi', 'angela', ' jnana'],
    "Marks" : [76,89,90]

}
data= pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')

