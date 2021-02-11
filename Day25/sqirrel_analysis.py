import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
sqirrel_black_count = len(data[ data["Primary Fur Color"] == 'Black'])
print(sqirrel_black_count)

sqirrel_gray_count = len(data[ data["Primary Fur Color"] == 'Gray'])
print(sqirrel_gray_count)

sqirrel_cinnemon_count = len(data[ data["Primary Fur Color"] == 'Cinnamon'])
print(sqirrel_cinnemon_count)

data_dict = {
    "Fur_color" : ["Gray","Black","Cinnemon"],
    "Count": [sqirrel_gray_count,sqirrel_black_count,sqirrel_cinnemon_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_squirrel_data")