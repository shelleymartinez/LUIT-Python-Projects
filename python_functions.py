#!/usr/bin/env python3.7

# 1) Write a 'split-name' function that takes a string and returns a dictionary with first_name and last_name
def split_name(name):
    first_name, last_name = name.split(maxsplit=1)
    return {
        'first_name': first_name,
        'last_name': last_name,
    }
    
assert split_name("Sammy Davis") == {
    "first_name": "Sammy",
    "last_name": "Davis",
}, f"Expected {{'first_name': 'Sammy', 'last_name': 'Davis'}} but received {split_name('Sammy Davis')}"

# 2) Ensure that 'split_name' can handle multi-word last names

assert split_name("Sammy Davis Junior") == {
    "first_name": "Sammy",
    "last_name": "Davis Junior",
}, f"Expected {{'first_name': 'Sammy', 'last_name': 'Davis Junior'}} but received {split_name('Sammy Davis Junior')}"

# 3) Write an 'is_palindrome' function to check if a string is a palindrome (reads the same from left-to-right)
def is_palindrome(item):
    item = str(item)
    return item == item[::-1]
    
    
assert is_palindrome("radar") == True, "Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, "Expected False but got {is_palindrome('stop')}"


# 4) Make 'is_palindrome' work with number

assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"
    
# 5) Write a 'build_list' function that takes an item and a number to include in a list
def build_list(item, count=1):
    items = []
    for _ in range(count):
        items.append(item)
    return items

assert build_list("Tesla", 3) == [
    "Tesla",
    "Tesla",
    "Tesla",
], f"Expected ['Tesla', 'Tesla', 'Tesla'] but received {repr(build_list('Tesla', 3))}"
assert build_list("Lucid") == [
    "Lucid"
], f"Expected ['Lucid'] but received {repr(build_list('Lucid'))}"