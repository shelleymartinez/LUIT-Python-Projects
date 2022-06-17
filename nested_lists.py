#!/usr/bin/env python3.7

#HackerRank challenge nested lists

#Create a list of student and grade, and another list of all the records together
record = []
record_list = []

#Enter number of students to put in a list
number = int(input("Enter number of students to put in a list: "))

#Create a list of records by entering student's first name and grade, interating till number is reached
for _ in range(1, number + 1):
    student_name = input("Enter student's first name: ")
    grade = float(input("Enter " + student_name +"'s" + " grade: "))
    record = [student_name, grade]
    record_list.append(record)

#Create variable for second lowest grade   
x = 99999 
for i in range(len(record_list)):
    if x > float(record_list[i][1]):
        x = float(record_list[i][1])

y = 999999
for i in range(len(record_list)):
    if float(record_list[i][1]) > float(x) and y > float(record_list[i][1]):
        y = float(record_list[i][1])

#Print names of students with second lowest score in alphabetical order        
secondary = []
for i in range(len(record_list)):
    if float(record_list[i][1]) == float(y):
        secondary.append(record_list[i][0])
    secondary = sorted(secondary)
    
for i in range(len(secondary)):
        print(secondary[i])