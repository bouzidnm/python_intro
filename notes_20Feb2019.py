## Notes for 20 Feb 2019
## Lists, Indexing, Slicing

## Lists
## Square brackets, are ordered and changeable
nums = [1, 2, 3, 4, 5] #same element types, int
fruit = ['apple', 'banana', 'strawberry'] #same element types, str
random = ['bob', 2, 3.14, True]

# Review from last week
type(nums)
# it's a class list

## Indexing
## data going forward always start at 0
## data doing backwards always start at -1
#variable_name[index]
s = "PYTHON"
# index the string s
s[0] #first letter, p
s[-1] #last letter, n

# Indexing exercises
s = 'hello world!'
# first letter, h
s[0]
s[-12]
s[-len(s)]
# get length of string
len(s)
s[len(s)-1] # forwards, get end of string, '!'
s[-len(s)] # backwards, get beginning of string, 'h'

# double indexing; usually won't see anything more than triple indexing
# add another set of brackets
# get 'a' in 'apple'
fruit[0][0]

# indexing lists
animals = ['dog', 'cat', 'bird', 'fish']
animals[2] # grabs 'cat'
animals[2][1] # grabs 'a' in 'cat'

## Slicing
## grab multiple values with a colon
## Format: variable_name[index : index]
## grabs everything up until, BUT NOT INCLUDING, the second index

# Slicing strings
s = 'hello world!'
s[0:2] # grabs the first 2 letters
s[1:5] # grabs 'ello'
s[1:6] # grabs 'ello ' with space
s[3:] # grabs everything from 'l' to end, s[3:], 'lo world!'

# Slicing lists
fruit = ['apple', 'banana', 'strawberry', 'orange']

## Lists within lists
## lists can have other lists as elements
family = [['bob', 21], ['dave', 24], ['emma', 19], ['jen', 22]]
family[0][1] # bob's age
family[0][0][0] # 'b' in 'bob', shouldn't do more than triple

## another example
lol = [['dog', 'cat', 'bird'], ['car', 'boat', 'plane'], ['red', 'yellow', 'green']]
## ecology for a crowded plant, LMM and R