# ### VARIABLES: containers for storing data values
# # they are case sensitive
# # they follow a sequence that is it will print the last line be4 print
# x = 22
# print(x)
# # to check the type
# type(x)
# y = "How are you doing?"
# print(y)
# type(y)
# # to Overide previous variable
# y = "I am good"
# print(y)
# # assigning multiple value to multiple variable
# x,y,z = "we", "are", "happy"        # x=we, y=are, z=happy
# print(x)
# print(y)
# print(z)
# # assinging multiple variables to 1 value
# a = b = c = "Happy Weekend"
# print(a)
# print(b)
# print(c)
# #####
# ice_cream = ["chocolate", "vanila", "rocky road"]
# x,y,z = ice_cream
# print(x)
# print(y)
# print(z)

# ## How to name a variable
# # camel case
# #test variable case
# testVariableCase = 1
# # pascal case
# #test variable case
# TestVariableCase = 1
# # snake case
# #test variable case
# test_variable_case = 1
# # you can do
# testvar = 4
# test_var = 4
# testVar = 4
# TestVar = 4
# testVar2 = 4
# #dosent work
# 2testvar = 4
# test-var = 4
# test var = 4
# test,var = 4
# # adding two string together
# v = "Today is going tobe a good day" + "."
# print(v)
# # add an integer together 
# # note integer and string cannot be added together
# i = 3 + 5
# print(i)
# #
# x = "Monday "
# y = "Tuesday"
# z = " Wednessday"
# print(x+y+z)
# a = 3
# b = 4
# c = 5
# print(a+b+c)
# to print two variable with diffrent value we use the ,
# a = 2
# b = "Days"
# print(a,b)

# Data Types: classification of stored data and it tells us what operation can be performed on the data
# numeric, sequence type, set, boolean, and dictionary
# numeric- integers, float and comlex numbers
# integers are whole numbers either positive or negative
# type(12)        # int
# type(-12)       #int
# type(-12 + 60)  #int
# type(10.5)      #float
# type(2 + 12.45) #float
# type(10 + 3j)   #complex   j is the only compex number
## Boolean
# type(True)          #bool
# type(1 > 5)         #bool
# y = 1 > 5
# print(y)
# y = 1 == 1
# print(y)
## sequence type data types
# string
'single quote'
"double quote"
"""
multiline/triple quote
"""
# to use a quote or apostrop in a sentence 
"I've always wanted a cat"
# or use a triple quote

#####  Conditional Statement: certain conditions need to be met b4 we can accomplish some part of code
# name = "John"
# num = 8
# if name is "John":
#     print("That is my name")
#     ###or
# if name == "John":
#     print("That is my name")
# if name is "Joy":
#     print("My name is Joy")            #code wount run
# elif name == "John":
#     print("My name is John")

# if 6 == 6:
#     print("the number is 6")
# else:
#     print("the number is not 6")
####
# if name is "Joy" and num == 5:
#     print("My name is Joy")            #code wount run
# elif name == "John" or num == 9:
#     print("My name is John")
# elif name == "Don":
#     print("My name is Don")
# else:
#     print("Name dose not exist")

##### LOOPS: used to create repitition
# for number in range(3):
#     print("Cool", number + 1, (number + 1)*".")
    ##or
# for number in range(1, 4):
#     print("Cool", number, number * ".")
    ### pass a 3rd argument as a step
# for number in range(1, 10, 2):
#     print("Cool", number, number * ".")
#####
# success = False
# for number in range(3):
#     print("Cool")
#     if success:
#         print("Congratulations")
#         break
# else:
#     print("Fail")
### nested loop
# for x in range(5):              #it will be executed 5 times
#     for y in range(3):              # it will be executed 3 times
#         print(f"({x}, {y})")
# # iterable
# for x in range(5):
#     print(x)
# # string
# for x in "Python":
#     print(x)
# #list
# for x in [1, 2, 3, 4, 5]:
#     print(x)
# # ex
# count = 0
# for number in range(1, 20):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print("We have {count} even numbers")

#### TYPECASTING: the process of converting a value of one data type to another 
# #(string, integer, float, boolean)
# Explicit vs Implicite
# Explicit
# name = "Guy"
# age = 25
# rate = 7.5
# sings = True
# # to check the data type
# print(type(name))
# print(type(age))
# print(type(rate))
# print(type(sings))
# # to convert age(int) to float
# age = float(age)
# print(age)
# print(type(age))
# # to convert rate(float) to int
# rate = int(rate)
# print(rate)
# print(type(rate))
# # to convert sings into string
# sings = str(sings)
# print(sings)
# print(type(sings))
# # to convert age(int) to boolean
# age = bool(age)                 # anything other than zero is true
# print(age)
# print(type(age))
# # to convert name(string) to boolean
# name = bool(name)                 # anything other than an empty string is true
# print(name)
# print(type(name))
# # implicit
# x = 2
# y = 2.1
# x = x / y
# print(x)

# count = 0
# for number in range(1, 21):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers in this range.")
# This code will print all even numbers from 1 to 20 and then the total count.

#######     FUNCTIONS AND BUILT IN FUNCTIONS
# collection of instruction or code
# def func():
#     print("The first function")
#     print("The second function")
# print("The last functions")
# func()          # to call the function block
# funcion in mapping by inputing an argument
# def func1(x):
#     return 2*x
# a = func1(5)
# print(a)
# # two argument
# def func1(a, b):
#     return a + b
# b = func1(3, 6)
# print(b)
# #####
# def func1(x):
#     print(x)
#     print("The above is the value of x")
#     return 5*x
# c = func1(9)
# print(c)
# ###### Arbituary argument
# def num_arg(*num):
#     print(num[0]*num[1])
# num_arg(6,5,7,2,4)
# ## or
# args_tuple = (6,5,7,2,4)
# def num_arg(*num):
#     print(num[0]*num[1])
# num_arg(*args_tuple)
# ########## Arbituary Keyword Arguments
# def num_kwarg(**num):
#     print(f"The number is: {num["integer"]} The other number: {num["integer2"]}")
# num_kwarg(integer = "2500", integer2 = "350")
# #########
# def score_func(name, student_score, total_score):
#     ave = student_score/total_score*100
#     print("Average score: ")
#     print(ave)
#     if ave < 50:
#         print(f"{name} did not pass")
#     else:
#         print(f"{name} passed")
# score_func("Troy", 15, 70)

###### Built-in Functions
# ### Math function
# # bool - values are true and false
# #  int - convert an argument like string into integer 
# string_num = "12345"
# conv_num = int(string_num)
# print(conv_num)
# #  float - convert an argument to float
# string_num = "12345.67"
# conv_num = float(string_num)
# print(conv_num)
# #  complex
# real_part = 1.5
# img_part = 5.5
# complex_num = complex(real_part, img_part)
# print(complex_num)
# # max
# num = [3, 4, 5, 6, 7, 8, 9]
# print(max(num))
# #  min
# num = [3, 4, 5, 6, 7, 8, 9]
# print(min(num))
# ## divmod - use to calculate quotient and reminder
# # quotient, reminder = 10 // 3, 10 % 3
# quotient, reminder = divmod(10, 3)
# print(quotient, reminder)
# #  abs - absolute power of a number
# print(abs(-10.5))
# print(abs(6+3))
# #  pow - calculate the power
# print(pow(2, 4))  ###(2**4)
# print(pow(2, 4, 3))  ###(2**4) % 3
# #  round - to round a number up
# print(round(2.675, 2))
# print(round(46584335, -5))
# #  sum - round up arbituary element
# num = [3, 4, 5, 6, 7, 8, 9]
# print(sum(num))
# even_num = sum(1 for x in num if x % 2)
# print(even_num)
### Collections
# dict
# list
# tuple
# set
# frozenset
# ### Strings and Bytes Builltins
# # bytes
# data = bytes(b"Hello")
# print(len(data))
# print(data[0])
# # bytearrays
# data = bytearray(b"Hello")
# print(len(data))
# print(data[2])
# # str - convdert to string
# num = 42
# str_conv = str(num)
# print(str_conv)
# print(type(str_conv))
# # memoryview
# # open - to open a file
# # chr
# print(chr(128512))
# # ord
# print(ord("H"))
# # bin,
# print(bin(72))
# print(int("0b1001000", 2))
# # oct
# print(oct(72))
# print(int("0o110", 8))
# # hex
# print(hex(72))
# print(int("0x48", 16))
# # format
# # input
# # name = input("Enter your name: ")
# # print(f"My name is {name}")
# # ascii, 
# print(ascii("Hello"))
# print(ascii("😀"))
# # repr
# print(repr("Hello"))
# print(repr("😀"))
# ##### Iteration
# # iter, next, iter, anext 
# iterator = iter([1, 2, 3, 4])
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# #
# for x in [1, 2, 3]:
#     print(x)
# # enumerate, 
# colors = ["pink", "red", "orange"]
# enumerate_color = list(enumerate(colors))
# print(enumerate_color[0])
# print(enumerate_color[1])
# print(enumerate_color[2])
# #
# for index, color in enumerate(colors):
#     print(index, color)
# # zip, 
# num = [1, 2, 3, 4, 5]
# alpha = ["a", "b", "c", "d", "e"]
# zipped = list(zip(num, alpha))
# print(zipped[0])
# print(zipped[1])
# print(zipped[2])
# print(zipped[3])
# print(zipped[4])
# #
# for number, letter in zip(num, alpha):
#     print(number, letter)
# # reversed, 
# num = [1, 2, 3, 4, 5]
# print(list(reversed(num)))
# #
# for x in reversed(num):
#     print(x)
# # sorted
# nums = [2, 5, 8, 6, 3, 1, 4, 7]
# print(sorted(nums))
# # filter, 
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_num = list(filter(lambda x: x % 2, num))
# print(even_num)
# #
# even_num = [x for x in num if x % 2]
# # map, 
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square_num = list(map(lambda x: x ** 2, num))
# print(square_num)
# #
# square_num = [x**2 for x in num]
# # all, any
# # range, slice
# ###### Debugging
# # breakpoint
# def break_point():
#     for i in range(5):
#         if i == 3:
#             breakpoint()
#         print(i)
# # help
# print(help(str))
# # print
# print("Hi There")

########    MODULES ########
# A file containing code you want to include in your program
# "import" is use to include a module (built-in or our own)
# useful to break up large program reusable seperate files
# to access python libary modules we use <print(help("modules"))> 

# # to import a moudule
# import math
# # to access the math module
# math.pi
# # or
# import math as m
# m.pi
# # or
# from math import pi
# a, b, c, d, e = 1, 2, 3, 4, 5
# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)
# print(math.e ** e)
# Create a module
# # create a new fie e.g example.py
# pi = 3.14159
# def square(x):
#     return x**2
# def cube(x):
#     return x**3
# def circumference(radius):
#     return 2 * pi * radius
# def area(radius):
#     return pi * radius ** 2
# ### within our main file we import
# import example
# result = example.pi
# result = example.square(3)
# result = example.cube(3)
# result = example.circumference(3)
# result = example.area(3)
# print(result)

# ####### DECORATORS  ####
# # A function that extends the behaviour of another function with or without modifying the base function
# # we passes the base function as an argument to the decorator
# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("You add sprinkles")
#         func(*args, **kwargs)
#     return wrapper
# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("You add fudge")
#         func(*args, **kwargs)
#     return wrapper
# @add_sprinkles      # to add the above decorator
# @add_fudge
# def get_ice_cream(flavour):
#     print(f"Your {flavour} ice-cream is ready")
# get_ice_cream("Vanila")

##########  ITERATOR    #########
# from typing import Iterable, Iterator
# people: list[str] = ["joy", "liam", "dan"]
# people_iter: Iterator[str] = iter(people)
# print(next(people_iter))
# print(next(people_iter))
# print(next(people_iter))
# # iterable
# def say_hello(names: list([str])) -> None:
#     for name in names:
#         print(f"Hello {name}")
# say_hello(("joy", "liam", "dan"))

####### REGULAR EXPRESSION  ########
# use to identify and specify a pattern of characters that we are looking for in our text
# Re Module + Regex Methods
#   Function                    Description
# findall               Returns a list containing all matches
# search                Returns a Match object if there is a match anywhere in the string
# split                 Returns a list where the string has been split at each match
# sub                   Replace one or many matches with a string
import re
quote = "Because of its strong structuring constructs (nested code blocks, functions, classes, modules, and packages) and its consistent use of objects and objectoriented programming, Python enables us to write clear, logical applications for small and large tasks."
print(re.search("and", quote))
print(re.search("and", quote).group())
print(re.findall("and", quote))
print(len(re.findall("and", quote)))
print(re.split("/,", quote))
print(re.sub("and", "or", quote, count=1))
print(re.sub("and", "or", quote))
# to specify uppercase
pattern = re.compile("^[A-Z]+$")
print(pattern.search("Hello World"))
print(pattern.search("HELLO WORLD"))
print(pattern.search("HELLOWORLD"))
# to specify lowercase
pattern = re.compile("^[a-z]+$")
print(pattern.search("Hello World"))
print(pattern.search("hello world"))
print(pattern.search("helloworld"))
# to specify all case
pattern = re.compile("^[a-zA-Z\s]+$")
print(pattern.search("Hello World"))
print(pattern.search("hello world5"))
print(pattern.search("helloworld"))