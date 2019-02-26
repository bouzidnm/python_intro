## Notes for 18 Feb 2019
## Printing, Data Types, String inputs

# Print output
print(1+6)
print(1 + 6)
print(5 ** 2) # ** is raised to a power of

# Notes with a hashtag

# Addition, subtraction, multiplication, division
    # When doing division it always returns a decimal place
    # Python follows PEMDAS

# Data types
    # check with
type(128)
    # Integer
        # 'int', number without decimal
    # Float
        # 'float', number with decimal
    # String
        # 'str', can create with single or double quotes, space sensitive
        # can be a number
    # Boolean
        # 'bool', True or False, only first letter capitalized

# Data type conversions
str(5) # convert to strong
int(5) # convert to integer
float(5) # convert to float

# Variables
    # Can't have any spaces in the variable
x = 5 # int
y = False # bool
name = 'bob' # string

# User input
    # Allow user to manually enter in a value for a variable
name = input('My name is: ') # include string so the user knows what to do
name = input() # it's just blank and waits for input
name = input('Enter your name: ')  # include string so the user knows what to do
age = input('My age is: ')
    # input always returns as a string!

# Variable filling
    # Call variables with {} (curly braces) when using .format with a string
    # .format is not in the '' (quotes)
name1 = 'Peter'
age1 = 49
name2 = 'Emilia'
age2 = 31
print('My name is {} and I am {} years old.'.format(name1, age1))

# Exercises: Variables Part 1
my_name = input('Enter your name: ')
fav_food = input('Favorite food: ')
print('My name is {} and my favorite food is {}.'.format(my_name, fav_food))

# Exercises: Variables Part 2
day = input('Day of the week: ')
name1 = input('Who paid: ')
name2 = input('Who ate: ')
restaurant = input('Where did they go? ')
print('On {} night, {} took {} out to dinner at {}.'.format(day, name1, name2, restaurant))
    # don't need to add print() if you're in the console, but for it to print from a script you do
