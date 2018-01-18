'''

01a Exercises
These exercises should help you get the flavor of how to perform arithmetic and string operations in Python. 
You will also get to play with (pseudo-)random generators and the range operator.
These skills will all be used in assignment 2.

To answer these exercises, open the IDLE program that came with your Python installation. IDLE is a line-by-line Python interpreter.
You can copy lines from this file into IDLE to interpret them and produce a result. Then copy the result back to the following line in this file (after the #).
You will also need to answer several questions to show you understand what is happening. 


'''
# Math in Python is what you would expect. Add comments with the answers the IDLE returns. I'll do the first one for you.
10 + 15 
#25
8 - 1 
#7
10 * 2 
#20
35 / 5
#7

35 / 4
#8.75
35 // 4 
#8
# What is the difference between the / operator and the // operator?
# // removes the decimal point, which is integer division

2 ** 5 
# 32
# What does the ** operator do?
# takes a number to the power of another number
5 % 3 
# 2
5 % 2
# 1
5 % 4
# 1
# What does the % operator do?
# returns the remainder when the number before the % is divided by the number after

(1 + 3) * 2
# 8
# What effect do the parenthesis have on this statement?
# They create an order of operations for the statement

# Data in python is of different flavors or "types," each with its own characteristics
type(3)
# <class 'int'>
type(3.0)
# <class 'float'>
type("word")
# <class 'str'>
type(True)
# <class 'bool'>
type(False)
# <class 'bool'>
type(None)
# <class 'NoneType'>
# None is a special object in python. We will talk more about it later


# It is possible to convert from one type to another. 
int(3.0)
#3
float(7)
#7.0
str(55)
# '55'
bool(1)
# True
# How can you tell the difference between these four different types?
# decimal indicates float, no decimal indicates int, string has quotes, bool is either False or True

# Strings are created with single or double-quotes
"This is a string."
'This is also a string.'

"Hello " + "world!"
# What does the + operator do here?
# appends the second string to the end of the first string

"This is a string"[0]
#'T'
"This is a string"[5]
#'i'
"This is a string"[8]
#'i'
# What is happening as you change the number?
# This number indicates the character returned by the function. 0 returns the first character of the string
#  5 returns the sixth character, and 8 returns the ninth character.

"This is a string"[-1]
# 'g'
# What happens when you use a negative number?
# It wraps around, instead returning the first character from the END of the string

"%s can be %s" % ("strings", "interpolated")
# 'strings can be interpolated'
# What is happening here? 
#  strings are substituted for the spots with %s; the first one in the first spot, the second in the second

# A more robust (and modern) way to put things into strings is using the format method
"{0} can be {1}".format("strings", "formatted")
# 'strings can be formatted'

# You can use names instead of numbers to make it easier to keep things straight
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
# 'Bob wants to eat lasagna'

# You have already met the print method
print("I'm Python. Nice to meet you!")
# Here is its sibling, the input method
n = input("What is your name? ")
print("Hello, " + n)
# What is your name? Blake
# Hello, Blake
# What just happened?
# My input was registered to memory as the variable n, which was referenced in the next line

# For your next assignment, you will need to use random numbers 
# first we need to get a few methods from the library called random
from random import random,randint,shuffle,sample
random()
# Run this line a few times. What is happening here?
# Returns a random number between 0 and 1

randint(1,100)
# How is this different?
# Returns a random integer in the range between 1 and 100

# The next few use a list of numbers from 0 to 9
items = [0, 1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)
# What just happened?
# Sorts the items in the list in random order

print(sample(items, 1))
# What does this do?
# Takes a random sample of one member of items

print(sample(items, 5))
# What does the second parameter control?
# Changes the number of items in the output list of sample

for i in range(0,5):
	print(i)
# 0
# 1
# 2
# 3
# 4
# What is happening here? What happens if you change the two range parameters?
# This line prints every possible "i" in the range between 0 and 5, not including 5 but including 0
# changing the two range parameters will change where the printing begins and ends
