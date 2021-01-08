travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

#  Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(count, visit, city):
    new_dictionary = {}
    new_dictionary["country"] = count,
    new_dictionary["visits"] = visit,
    new_dictionary["cities"] = city

    travel_log.append(new_dictionary)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



