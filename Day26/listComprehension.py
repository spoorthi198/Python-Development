print('hi')

new_list = [n+1 for n in range(1,5)]
new_list = [n*2 for n in range(1,5)]
names = ['alex', 'beth', 'caroline', 'dave', 'elanor', 'freddii']
names
['alex', 'beth', 'caroline', 'dave', 'elanor', 'freddie']
upper_names = [name.upper() for name in names if len(name)>5]
upper_names
['CAROLINE', 'ELANOR', 'FREDDIE']

numbers = [1,1,2,3,5,8,13,21,34,55]
result = [num for num in numbers if num % 2 == 0]

print(result)