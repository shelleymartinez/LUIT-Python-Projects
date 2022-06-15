#!/usr/bin/env python3.7
#HackerRank loop challenge

#read an integer
n = int(input("Type an integer: "))

#create list of integers less than n
my_range = range(n)
list(my_range)

#print the square of each integer in my_range
for value in my_range:
    print(value*value)