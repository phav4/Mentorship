# List : order, mutable, that allows duplicate elements
# myList = ["Banana", "apple", "orange"]

# print(myList)

#myList2 = list()
#print(myList2)

#myList3 = [5, True, "Apple", "Apple"] # list allow duplicate element
#print(myList3)

# To A access a list we use index
# -1: refers to the last item in the list
# -2: refers to the 2nd last item in the list
#item = myList[-1]
#print(item)

# To iterate over the list
#for i in myList:
#    print(i)

# to check if am item is in our list
#if "orange" in myList:
#    print("Yes")
#else:
#    print("NO")

# to check how many element is in our list
#print(len(myList))

# To appemd an item
#myList.append("lemon")
#print(myList)

# to insert an item at a specific postion
#myList.insert(1, "cherry")
#print(myList)

# # To remove an item
# items = myList.pop()
# print(items)
# print(myList)

# # to remove a specific element
# items = myList.remove("apple")
# print(myList)

# # remove all element in the list
# items = myList.clear()
# print(myList)

# # revers the list
# items = myList.reverse()
# print(myList)

# myList3 = [4, 3, 2, 1, -1, -2, -5, 10]
# print(myList3)

# # sort the list
# items = myList3.sort()
# print(myList3)

# new_list = sorted(myList3)
# print(new_list)

# # new list with multiple type
# myList4 = [0] * 5
# print(myList4)

# # adding two list together
# myList5 = [1, 2, 3, 4, 5]
# new_list = myList4 + myList5
# print(new_list)

# slicing
# if we dont specify a start index it start from the begining i.e [:5] it start from the begining
# # if we dont specify a stop index it start from the begining i.e [1:] it gose all the way to the end
# mylist6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# A = mylist6[1:5] 
# A = mylist6[::2]    #step index i.e it takes every second item
# A = mylist6[::-1]   #revers the list
# print(A)

# # Copying a list
# list_org = ["banana", "cherry", "apple"]
# list_cpy = list_org.copy()      #return the first list
# list_cpy = list(list_org)       #return the first list
# list_cpy = list_org[:]          #return the first list
# list_cpy.append("lemon")
# print(list_cpy)
# print(list_org)

# # List comprehension: create a new list from an exixting list
# a = [1, 2, 3, 4, 5, 6]
# b = [i*i for i in a]
# print(a)
# print(b)

#TULIP:   cant be change after setting, allows duplicates elements
#myTuple = "apple", "banana", 23, "cherry"     #() are optional and can be run without it
#myTuple = tuple(["apple", "banana", 23, "cherry"])    #or we can use tuple() constructor
#print(type(myTuple))   #to check the type
#print(myTuple) 

# to access a tuple we use index
#item = myTuple[0]   #-1 revers to the last item, -2 2nd last item
#print(item)

# new values cannot be assign to a tuple
#myTuple[0] = "lemon"   #this will give an error
#print(myTuple)

# we can loop through a tuple
#for i in myTuple:
#    print(i)
# to check if an item is in a tuple
# if "banana" in myTuple:
#     print("Yes")
# else:
#     print("No")

# to check how many element is in a tuple
# myTuple = ("a", "p", "p", "l", "e")
#print(len(myTuple))
#print(myTuple.count("p"))       #to count element
#print(myTuple.index("p"))       #to check index element

# #convert tuple to list
# myList = list(myTuple)
# print(myList)
# # convet back
# my_tuple = tuple(myList)
# print(my_tuple)

# slicing

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# b = a[1:5]
# b = a[1:]    #if we dont specify a stop index it gose all the way to the end
# b = a[:5]    #if we dont specify a start index it start from the begining
# b = a[::2]    #step index i.e it takes every second item   
# b = a[::-1]   #revers the list
# print(b)

# # unpacking a tuple
# myTuple = ("Max", 28, "cherry")
# name, age, fruit = myTuple
# print(name)
# print(age)
# print(fruit)
# myTuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# i1, *i2, i3 = myTuple
# print(i1)   #first item
# print(i2)   #all middle item
# print(i3)   #last item

## compare list and tuple
# import sys
# myList = [0, 1, 2, "apple", "banana", True]
# myTuple = (0, 1, 2, "apple", "banana", True)
# print(sys.getsizeof(myList), "bytes")   #size of the list in memory
# print(sys.getsizeof(myTuple), "bytes")  #size of the tuple in memory
# # we can see that tuple is smaller than list in memory
# # this is because list is mutable and tuple is immutable
# import timeit
# print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))   #time taken to create a list
# print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))   #time taken to create a tuple
# we can see that tuple is faster than list
# tuple are more memory efficient and faster than list


############Dictionary############
# unordered, key:value pair, mutable, no duplicate element
#myDict = {"name": "John", "age": 30, "city": "New York"}
#print(myDict)
#myDict2 = dict(name="Mary", age=33, city="Boston")   #or we can use dict() constructor 
#print(myDict2)
# to access a dictionary value
#value = myDict["name"]   #if the key is not found it will give an error
#print(value)
#to add a new key:value pair
#myDict["email"] = "john@xyz.com"
#print(myDict)

# we can do it again to update the prior value
#myDict["email"] = "cool@xyz.com"
#print(myDict)
# to delete an item
#del myDict["name"]
#print(myDict)
#myDict.pop("age")
#print(myDict)
#myDict.popitem()   #remove the last item
#print(myDict)

# check if a key exist
# if "name" in myDict:
#     print(myDict["name"])
# or
# try:
#     print(myDict["name"])
# except:
#     print("Error")

# to loop through a dictionary
#for key in myDict.keys():   #to get all the keys
#for value in myDict.values():   #to get all the values
#for key, value in myDict.items():   #to get all the key, values
#    print(value)
#for key, value in myDict.items():   #to get both keys and values
#    print(key, value)
# # to copy a dictionary
# myDict_cpy = myDict          #this will not return a copy of the first dictionary but point to the same location
# #print(myDict_cpy)
# myDict_cpy = dict(myDict)   #return the first dictionary
# myDict_cpy = myDict.copy()     #return the first dictionary
# #print(myDict_cpy)
# myDict_cpy["email"] = "feel@xyz.com"
# print(myDict)   #this will also change the original dictionary because both are pointing to the same location
# print(myDict_cpy)  #this will not change the original dictionary

# # Merging two dictionary
# myDict1 = {"name": "John", "age": 30, "email": "xyz@email.com"}
# myDict2 = {"city": "New York", "name": "Mary", "age": 33,}

# myDict1.update(myDict2)   #if there is a duplicate key the value of the second dictionary will overwrite the first
# print(myDict1)

# # Key types
# myDict = {1: "apple", 2: "banana", 3: "cherry"}   #integer keys
# print(myDict)

# # value = myDict[1]   #accessing value using key, we want to use the number 1 to access apple
# # print(value)

# myTuple = (8, 3)       #List cannot be used as key because it is mutable
# myDict = {myTuple: "apple", 2: "banana", 3: "cherry"}   #tuple keys
# print(myDict)

# # SETS: unordered, mutable, no duplicate element
# mySet = {1, 2, 3, 1, 2, 5}   #duplicate element will be removed
# print(mySet)
#mySet = set("Hello")   #or we can use set() constructor
#print(mySet)
#create an empty set
# mySet = {}   #this will create an empty dictionary
# mySet = set()   #this will create an empty set
# #print(type(mySet))
# mySet.add(1)
# mySet.add(2)
# mySet.add(3)

# mySet.remove(2)   #if the item is not found it will give an error
# mySet.discard(5)  #if the item is not found it will not give an error
# mySet.clear()     #remove all items
# print(mySet.pop())  
# print(mySet)
# iterate through a set
# for i in mySet:
#     print(i)

# to check if an item is in a set
# if 3 in mySet:
#     print("Yes")
# union and intersection
# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}
# # union combine both sets and remove duplicate element
# u = odds.union(evens)
# print(u)

# # intersectio return the common element in both sets
# i = odds.intersection(primes)
# print(i)
# diffrence of two set
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}
# items in setA but not in setB
# diff = setA.difference(setB)
# print(diff)
# # items in setB but not in setA
# diff = setB.difference(setA)
# print(diff)
# diff = setB.symmetric_difference(setA)  # return all element in A and B but not element in both set
# print(diff)
# to modify a set
# setA.update(setB)       #add the set in B to A without duplicating
# print(setA)
# setA.intersection_update(setB)       #update set by keeping only element found in both set
# print(setA)
# setA.difference_update(setB)       #remove the element found in another set
# print(setA)
# # Subset superset and disjoint
#setA = {1, 2, 3, 4, 5, 6}
# setB = {1, 2, 3}
# setC = {7, 8}
# print(setA.issubset(setB))      #i.e all element in A is in B
# print(setA.issubset(setB))      #i.e all element in B is in A
# print(setA.isdisjoint(setC))      #i.e both set have a null intersection
# copy a set
#setB = setA             #any change will affect the first set
#setB = setA.copy()      # .copy wont change the initial set after copying it
#setB = set(setA)        # would not change the initial set
#setB.add(7)
#print(setB)
#print(setA)
# Frozen set; imutable set i.e cannot be changed once created
# a = frozenset([1, 2, 3, 4])
# print(a)

####   STRING : order, immutable, text representation
# myString = "Hello World"        
# if we want to use ' inside '' we use the \ before the ' or use the double qoute, 
# tripple qoute for multiple line string(""" or ''')  \ use to to not continue in another line
# \ also use to escape special character like \n (new line), \t (tab space)
# myString = 'Hello \'World'
# print(myString)

# To access character/substring in a string
# char = myString[0]   #-1 revers to the last item, -2 2nd last item
# print(char)
# substring = myString[1:5]   #substring from index 0 to 4
# substring = myString[:5]    #if we dont specify a start index it start from the begining
# substring = myString[1:]    #if we dont specify a stop index it gose all the way to the end
# substring = myString[::2]    #step index i.e it takes every second item
# substring = myString[::-1]   #revers the list
# print(substring)
# # cocatinate to another string
# greeting = myString + " I am John"
# or
# name = "John"
# sentence = greeting + " I am " + name
# print(sentence)
# # iterate over a string
# for i in myString:
#     print(i)

# # check if a character/substring is in a string
# if "e" in myString:
#     print("Yes")
# else:
#     print("No")
# other way
# my_string = "   Hello World   "
# my_string = my_string.strip()   #remove space at the begining and end of the string
# print(my_string)
# myString = "Hello World"
# print(myString.upper()) # convert every charater to an uppercase
# print(myString.lower()) # convert every charater to an lowercase
# print(myString.startswith("H")) # chech if our string start with specific character/substring
# print(myString.endswith("World")) # chech if our string end with specific character/substring
# print(myString.find("o")) # find the index of a character/substring, return the index of the first one found, -1 if it is not found
# print(myString.count("o")) # count the number of character
# print(myString.replace("World", "Universe")) # Replace a character/substring, if not found it will return the initial string
# List and string
# myString = "How are you doing"
# myList = myString.split(" ")        #convert string to list, looks for space and divide it
# print(myList)
# newString = " ".join(myList)     # convert a list back to string
# print(newString)
# my_list = ["a"] * 6
# print(my_list)
# # to turn to a string
# # bad method
# # my_string = ""
# # for i in my_list:
# #     my_string += i
# # print(my_string)
# # instead use
# my_string = "".join(my_list)
# print(my_string)
# Format method: %, .format(), f-strings
var = "John"
var2 = 6
#myString = "The variable is %s" % var           # %s-for string, %d-for integer/decimal value, %f-for float;%.3f-to specify how many digit
# or
#myString = "The variable is {} and {}".format(var, var2)        # to specify float we use {:.2f}
# or the latest
# myString = f"The variable is {var} and {var2*2}"
# print(myString)

# COLLECTIONS: tpes are counter, namedtuple, orderedDict, defultdict, deque
# it implement special container data types, and provides altrnatives with some additional functionality compared to the general bert and containers like dictionaries, list, or tuples.
# Counter: it is a container that stores the element as dictionary keys and their count as dictionary values. 
from collections import Counter
# a = "aaaabbbbbbcccccccc"
# myCounter = Counter(a)
# print(myCounter)
# print(myCounter.items())        # gives only the item
# print(myCounter.keys())        # gives only the keys
# print(myCounter.keys())        # gives only the keys
# print(myCounter.most_common(1))        # gives the most comon
# print(myCounter.most_common(1)[0][0])        # gives the most comon element
# print(list(myCounter.elements()))        #  list all the element as list
# nametuple: easy to create lightweight object type, similar to astruct
from collections import namedtuple
# point = namedtuple("point", "v,z")
# pt = point(3, -9)
# print(pt)
# print(pt.v, pt.z)       # to Access the field
# orderedDict: like a regular dictionary but follow the order which they are inserted
from collections import OrderedDict
# ordered_dict = OrderedDict()
# ordered_dict["a"] = 1
# ordered_dict["b"] = 2
# ordered_dict["c"] = 3
# ordered_dict["d"] = 4
# ordered_dict["5"] = 5
# print(ordered_dict)
# defultdict: similare to dictionary but has a defult value if the key hasent bee set yet
from collections import defaultdict
# d = defaultdict(int)
# d["a"] = 1
# d["b"] = 2
# print(d)
# print(d["h"])   # to access the dictionary if it is not in the dictionary instead of returning an error it returns 0 
# deque: double ended queue and it is used for adding or removing element from both ends, and it is implement in a wAY THAT will be efficient
from collections import deque
# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(3)     # add element at the left side
#d.pop()     #remove last element
#d.popleft()     #remove element from left side
#d.clear()     #remove all element
#d.extend([4,5,6])
# d.extendleft([4,5,6])       # extend all element to the left side
# d.rotate(1)         # rotate all element 1 place to the right, -1 will rotate 1 place to the left
# print(d)

# ITERTOOLS: collection of tools for handling iterators. Iterators are datatypes used in for loop e.g list
# Types; product, permutations, combinations, accumulate, groupby, infinite iterators
# Product
from itertools import product
# a = [1, 2]
# b = [3, 4]
# prod = product(a,b, repeat=2)
# print(list(prod))
# Permutation
from itertools import permutations
# a = [1, 2, 3]
# perm = permutations(a, 2)
# print(list(perm))
# Combinations
from itertools import combinations, combinations_with_replacement       #To have repetition/combination with itself we use inations_with_replacemen
# a = [1, 2, 3, 4]
# comb = combinations(a, 2)
# print(list(comb))
# comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))
# Accumulate
from itertools import accumulate        #addition
import operator #multiplication
# a = [1, 2, 3, 4]
# acc = accumulate(a)
# acc = accumulate(a, func=operator.mul)      #this will multiply the element
# acc = accumulate(a, func=max)       # return the max for each comparissim
# print(a)
# print(list(acc))
# Groupby; returns keys and groups from an iterable
from itertools import groupby
# def smaller_than_3(x):
#     return x < 3
# a = [1, 2, 3, 4]
# go = groupby(a, key=smaller_than_3)
# go = groupby(a, key=lambda x: x<3)
# for key, value in go:
#     print(key, list(value))
    ###
# persons = [{"name": "Tin", "age": 25}, {"name": "Dan", "age": 25}, {"name": "Lisa", "age": 27}, {"name": "Claire", "age": 28}]
# go = groupby(persons, key=lambda x: x["age"])
# for key, value in go:
#     print(key, list(value))
## infinite iterators
from itertools import count, cycle, repeat
# count
# for i in count(10):
#     print(i)
#     if i == 50:
#         break
# cycle
# a = [1, 2, 3, 4]
# for i in cycle(a):
#     print(i)
# repeat
# a = [1, 2, 3, 4]
# for i in repeat(2, 4):            # will repeat 2, 4 times
#     print(i)

#####  LAMBDA: small one line function that is defined without a name
#### express as------ lambda arguments: expression
# add10 = lambda x: x * 10
# print(add10(5))
# using a function 
# def add_func(x):
#     return x * 10
#multiple argument
# mult = lambda x,y: x*y
# print(mult(2,7))
# to sort a list
# p2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# def sby(x):
#     return x[1]             # functions
# p2D_sl = sorted(p2D, key=lambda x: x[1])            # using lambda to sort with y(or the 2nd)
# p2D_sl = sorted(p2D, key=lambda x: x[0] + x[1])     # sort according to the sums of each tuples
# p2D_sl = sorted(p2D, key=sby)           # using funcction to sort
# print(p2D)
# print(p2D_sl)
#  Map functions: transform each element with a function
# map(function, sequence)
# a = [1, 2, 3, 4, 5]
# b = map(lambda x: x*2, a)       # to multiply each element in a by 2
# print(list(b))
# using list comprehension
# c = [x*2 for x in a]
# print(c)
# filter function: returns all element for which the function elevates to true
# filter(function, sequence)
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = filter(lambda x: x%2==0, a)       # to get even numbers 
# print(list(b))
# # using list comprehension
# c = [x for x in a if x%2==0]
# print(c)
# Reduced funcion: repetedly applies the function to the elements and returns a single value
# reduced(function, sequence)
# from functools import reduce
# a = [1, 2, 3, 4, 5, 6]
# product_a = reduce(lambda x,y: x*y, a)
# print(product_a)

### EXCEPTIONS and Error
# Syntax error: occurs when a syntactically incorect statement is detected
# Exceptions occures whan a statement is syntactically correct but still causes an error when it is executed
# e.g adding a number and a string together will raise an error
# a = 5 + "10"
# import modulethatdontexist     # module not found error
#name error
# a = 5
# b = c
# file not found error
# f = open("filedonotexist.txt")
#value error: function or oprator recives an argument that has the right type but an inappropriate value
# a = [1, 2, 3]
# a.remove(4)
# print(a)
#index error
# a = [1, 2, 3]
# a[4]
# print(a)
# myDict = {"name": "John"}
# myDict["age"]
# to force an exception when a condition is met we do that with the "raise" keyword
# x = -5
# if x < 0:
#     raise Exception("x should be positive")
# or
# assert(x>=0), "x is not positive"
# to handle exceptions with try
# try:
#     a = 5 / 0
# except:
#     print("Error")
# or
# try:
#     a = 5 / 0
# except Exception as e:
#     print(e)
####
# try:
#     a = 5 / 1
#     b = a * "10"
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("We good")
# finally:                            # will always run
#     print("Cleaning Up......")
## Defining our own exception
# class ValueTooHighError(Exception):
#     pass
# class ValueTooSmall(Exception):
#     def __init__(self, message, value):
#         self.message = message
#         self.value = value
# def testvalue(x):
#     if x > 100:
#         raise ValueTooHighError("Value is too high")
#     if x < 5:
#         raise ValueTooSmall("value too small", x)
# try:
#     testvalue(1)
# except ValueTooHighError as e:
#     print(e)
# except ValueTooSmall as e:
#     print(e.message, e.value)

#### LOGGING
import logging
logging.basicConfig()
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")