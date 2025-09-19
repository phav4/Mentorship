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
type(12)        # int
type(-12)       #int
type(-12 + 60)  #int
type(10.5)      #float
type(2 + 12.45) #float
type(10 + 3j)   #complex   j is the only compex number
## Boolean
type(True)          #bool
type(1 > 5)         #bool
y = 1 > 5
print(y)
y = 1 == 1
print(y)
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
name = "John"
num = 8
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

count = 0
for number in range(1, 21):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers in this range.")
# This code will print all even numbers from 1 to 20 and then the total count.