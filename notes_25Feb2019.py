## Notes for 25 Feb 2019
## Dictionaries

## unordered collection of keys and values
## written with curly brackets
## Format: dict_name = {key1: value, key2: value}
## when keys have multiple values, we put them in lists
## i.e. list of 'mammals' = ['cat', 'dog', 'horse']

## Grab values from dictionary using strings, not numbers
## dict[key]
car = {'brand': 'Ford', 'model': 'Mustang', 'color': 'black'}
car['brand'] # Ford

## Add value to existing dict
car['year'] = 1969

## Look at it
print(car)

## Delete a value
del(car['year']) # delete key/value pair

## Change a value
car['color'] = 'red'

## Creating Dictionaries
# Practice 1
keys = ['A', 'B', 'C', 'D', 'F']
values = [9, 12, 11, 5, 2]
# long way
test_grades = {'A':9, 'B':12, 'C':11, 'D':5, 'F':2}
# another way
test_grades = {keys[0]: values[0], keys[1]: values[1], keys[2]: values[2], keys[3]: values[3], keys[4]: values[4]}

# Practice 2
keys = ['name', 'age', 'grade']
values = [['Kevin', 'Sarah', 'Jaime'],
          [12, 10, 11],
          ['A', 'B', 'C']]
students = {'name':['Kevin', 'Sarah', 'Jaime'],
            'age':[12, 10, 11],
            'grade':['A', 'B', 'C']}
students = {keys[0]:values[0], # new line after comma makes code more visually pleasing
            keys[1]:values[1],
            keys[2]:values[2]}
print(students)

# Practice 3
keys = ['country', 'capital', 'population']
values = [['Argentina', 'China', 'Germany', 'India', 'Russia'],
 		  ['Buenos Aires', 'Beijing', 'Berlin', 'New Delhi', 'Moscow'],
		  [44.68, 1415.04, 82.29, 1342.51, 143.96]]
countries = {keys[0]:values[0],
            keys[1]:values[1],
            keys[2]:values[2]}

## Indexing/Slicing Dictionaries
# Grab Argentina
countries['country'][0]
# Grab 1415.04
countries['population'][1]
# Grab last 3 capitals
countries['capital'][2:]
# Grab Buenos in Bueno Aires
countries['capital'][0][0:6]
# Grab Delhi in New Delhi
countries['capital'][3][4:]
# Grab man in Germany
countries['country'][2][3:6]
# Grab cow in Moscow
countries['capital'][-1][-3:] # indicies can be negative but need to be in the same order you would read
# Ex: -1:-3 doesn't return anything
