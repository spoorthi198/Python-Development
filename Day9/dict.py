dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key in dict:
    dict[key] +=1

dict[1] = 4

print(dict[1])
dict["c"] = [1,2,3]
print(dict)