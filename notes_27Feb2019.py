## Notes for 27 Feb 2019
## For loops; .append(); .keys(); .values()

## Used to iterate over a sequence of values; to simplify redundant code
## Print out each item of a list individually
my_list = ['A', 'B', 'C', 'D', 'E']

## Two types of for loops
### Easy way: prints item
for i in my_list: # 'i is a variable that changes after every loop
    print(i)
    # line after a colon (:) is indented

## range() function allows you to loop a specified number of times
for i in range(5): # loop 5 times; remember it starts at 0!
    print(i)
### Other way: prints index of list
for i in range(5):
    print(my_list[i]) # now it prints elements of the list instead of 0:4

## Exercises
# Practice 1
names = ['Leo', 'Jen', 'Matt', 'Chris', 'Jess', 'Megan', 'Tom', 'Will']
# Print list by item
for i in names:
    print(i)
# Print list by index
for i in range(len(names)): # could also be range(8)
    print(names[i])

# Practice 2
names = ['Leo', 'Jen', 'Matt', 'Chris', 'Jess', 'Megan', 'Tom', 'Will']
ages = [43, 28, 48, 37, 21, 32, 22, 50]
# Print name and corresponding age with index
for i in range(8):
    print(names[i], ages[i])
# Use a for loop to print out a string for each person in the list
for i in range(8):
    print('{} is {} years old.'.format(names[i], ages[i]))

## .append() function; adds an item to the end of an existing list
## Format: list_name.append('thing to append')
names = [] # create an empty list
names.append('Sam')
print(names) # now there's one
names.append('Pat')
print(names) # now there's two
names.append('Julie')
print(names) # now there's three

## Back to Dictionaries
grades = {'A':9, 'B':12, 'C':11, 'D':5, 'F':2}
.keys() # returns keys of dictionary
.values() # returns values of dictionary
## Format: dict_name.keys(); dict_name.values()
# Create list of keys of dictionary
list = [] # empty list
for i in grades.keys(): # empty parentheses; loop by item
    list.append(i)
print(list) # notice indenting. Un-indenting stops the for loop

## Filling dictionaries the short way
## Recall: long way is dict['key1'] = 'value1'; dict['key2'] = 'value2'; etc.
# Initialize dictionary
grades = {}
for i in range(5):
    grades[keys[i]] = values[i]
print(grades)
## This only works if the lists have the same length

# Practice 3
keys = ['brand', 'model', 'year']
values = [['BMW', 'Nissan', 'Toyota'], ['M3', 'Skyline', 'Supra'], [2005, 1999, 2002]]
# Create empty dictionary called legend_cars
legend_cars = {}
# Use a for loop to fill dictionary with list of keys and values
for i in range(len(keys)):
    legend_cars[keys[i]] = values[i]
# print the dictionary
print(legend_cars)