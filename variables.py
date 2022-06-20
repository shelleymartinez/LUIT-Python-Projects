#!/usr/bin/env python3.7

# .format() method
first_name = "Tom"
last_name = "Cruise"
print("The main actor in Top Gun is {} and his last name is {}".format(first_name, last_name))

# f strings method
first_name = "Tom"
last_name = "Cruise"
print(f"The main actor in Top Gun is {first_name} and his last name is {last_name}")

#using number variables in a string, you can't add a string and a number together. You will have to turn the integer into a string
my_int = 50
sentence = "The total comes to: "

print(sentence + str(my_int))

# creating a dictionary by assigning the key-values
user = {"first_name":"Sara"}
print(user)

# To read the value associated with a key, you need to provide the name of the dictionary and the the value of the key inside square brackets.
user = {"first_name":"Sara"}
print(user["first_name"])

# To add an additional key-value to a dictionary, provide the dictionary name, the new key in [] and a value after an = sign.
user["family_name"] = "Sue"
print(user)

# To modify a value is similar to adding it
user["family_name"] = "Stuart"
print(user)

# To remove a key-value pair use the del statement with the name of the dictionary and the key you want to delete
del user["family_name"]
print(user)

# To read an element from a list you use the index number of the stored value
fruit = ["apples","oranges","bananas"]
print(fruit[1])

# To find the length of a list use len()
len(fruit)

# To return the last value in a list or work backwards from the last item using a negative index value
print(fruit[-1])
print(fruit[-2])

# use append() to add an element to the end of the list
fruit.append("kiwi")
print(fruit)

# add an element at a specific point in the list you can use the index value with the insert() method
fruit.insert(2, "passion fruit")
print(fruit)

# sort a list, but retain the original order of the list, you can use the sorted() function.
print(sorted(fruit))
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']

# to permanently sort the list, you should use the sort() method
fruit.sort()
print(fruit)

# reverse the order of a list use the reverse() method
fruit.reverse()
print(fruit)

# remove elements from a list using the del statement with index
del fruit[1]
print(fruit)

# use the remove() method to specify the value of the element you want to remove
fruit.remove('bananas')
print(fruit)

# type() method tells you what type of data python has stored in a variable
my_variable = "A string"
print(type(my_variable))















