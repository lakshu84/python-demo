# Collections Type
# contain elements of one or more data types
# order, mutability
# Lists: ordered, mutable

# To create a Lists
# fruits = ["apple", "pear", "cherry", "banana", "grape"]
# print(fruits[-2])
# print(fruits[1:-1]) #slicing 
# print(fruits[:])
# print(fruits[:-1])
# print(fruits[0:-1:1])
# print(fruits[::-1]) # Reversing

# Nested Lists
# fruits = [["apple", "pear", "cherry"], ["banana", "grapes"]]
# print(fruits)

# fruits.append('blackcurrent')
# print(fruits)

# fruits.insert(2, 'blackcurrent')
# print(fruits)

# fruits = ["apple", "pear", "cherry", "banana", "grapes"]
# fruits.append(['blackcurrent', 'strawberr', 'mango'])
# print(fruits[5])

# fruits = ["apple", "pear", "cherry", "banana", "grapes"]
# fruits.pop(3)
# print(fruits)

# from itertools import count
# from xml.dom import InvalidAccessErr
# from xml.dom.minidom import Element


# fruits = ["apple", "pear", "cherry", "banana", "grapes"]
# fruit1 = fruits.pop(3)
# print(fruits)


# fruits = ("apple", "pear", "cherry", "banana", "grape", "blackcurrent", "mango", "strawberry", "pear", "banana", )
# fruits.extend(['blackcurrant', 'strawberry', 'mango'])
# fruits1 =fruit.pops(3)
# del fruits[3]
# fruits[2] = "strawberry"
# fruits.sort(key=len, reverse = True)
# list2 = sorted(fruits, key =len, reverse = True)
# fruits.sort (key=fruits.count)
# print(fruits.count("pears"))

# # print(fruits.index())

# def find_all_indices(1: list, Element) -> list:
#     indices = []
#     for i in range(len(1)):
#         if 1[i] == element:
#             indices.append(i)
#     return indices 

# print(find_all_indices(fruits, 'pear'))

# Dictionaries: mutable, ordered 
# store assp
from ossaudiodev import SOUND_MIXER_DIGITAL2


cap_cities = {"UK" :"London", "France": "Paris", "Germany" : "Berlin"}
# cal_cities2 = dict(Belgium = "Brussels", Germany = "Berlin", Spain = "Madrid")
cap_cities["Netherlands"] = "Amsterdam"
# cap_cities.update(Poland = "Warsaw", Greece = "Athens")
# print(cap_cities.pop("UK"))
# del cap_cities["France"]
print(list(cap_cities.values()))
print(list(cap_cities.items()))
# print(cap_cities)

# Sets: unordered and, mutable, cannot store duplicates
set1 = {1, 2, 3, 5} 
set2 = set()
set2.add("hello")
set2.add("world")
set2.add("sample text")
set2.add("hello")
set2.add("sample text")

# set2.remove("hello")
#set.discard("blahbalhbalh")
print(set2)