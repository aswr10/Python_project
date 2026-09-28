'''
 What is File Reading?
 Reading a file means retrieving data stored in a file and using it within a program.
 '''
# # file = open("sample.txt", "r")
# # content = file.read()
# # print(content)
# # file.close()

# # """
# # Using with Statement
# # """
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)

# # '''
# # 2. Write Text File
# # What is File Writing?
# # Writing creates a new file or overwrites an existing file.
# # '''
# with open("sample.txt", "w") as file:
#     file.write("Welcome to Python")


# # '''
# # Example
# # '''
# # name = "Aswathy"

# # with open("sample.txt", "w") as file:
# #     file.write(name)

# # '''
# # 3. Append Text File
# # What is Appending?
# # Appending adds data to an existing file without removing previous content.
# # '''
# with open("sample.txt", "a") as file:
#     file.write("\nNew Record")

# '''
# 4. Largest Element in a List
# Problem Statement
# Find the largest number from a list.
# ''' 
# numbers = [15, 42, 8, 90, 33]

# largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         largest = num

# print("Largest:", largest)
# '''
# Built-in Function
# '''
#print(max(numbers))

# '''
# 5. Count Words
# Problem Statement
# Count the number of words in a sentence.
# '''
# sentence = "Python makes programming easy"

# words = sentence.split()

# print("Word Count:", len(words))

# '''
# Count Words in a File
# '''
# with open("sample.txt", "r") as file:
#     text = file.read()

# word_count = len(text.split())

# print("Words:", word_count)

# '''
# 6. Find Duplicates
# Problem Statement
# Find duplicate values in a list.
# '''
# numbers = [1, 2, 3, 4, 2, 5, 1]

# duplicates = []

# for item in numbers:
#     if numbers.count(item) > 1 and item not in duplicates:
#         duplicates.append(item)

# print("Duplicates:", duplicates)

# '''
# 7. What is an Algorithm?
# Definition
# An algorithm is a step-by-step procedure used to solve a problem.

# Characteristics of Algorithms

# Finite
# Clear and unambiguous
# Produces output
# Efficient

# Example Algorithm: Find Largest Number

# Assume first element is largest
# Compare with remaining elements
# Replace if larger element found
# Display largest value
# '''
# '''
# 8. Time Complexity Basics
# What is Time Complexity?
# Time Complexity measures how execution time grows as input size increases.
# Common Complexities

# Complexity     Name        Example
# O(1)        Constant    Access array element
# O(log n)    Logarithmic Binary Search
# O(n)        Linear      Linear Search
# O(n log n)  Efficient   Sorting (Python sort())
# O(n²)       Quadratic   Bubble Sort
# '''

# '''
# Example O(n)
# '''
# n=10
# for i in range(n):
#     print(i)

# '''
# Module 2: Searching & Sorting Algorithms
# Learning Objectives:

# Perform searches in data collections
# Understand sorting concepts
# Implement common searching and sorting algorithms
# Compare algorithm efficiency
# '''
# '''
# 1. Linear Search
# Definition
# Linear Search checks each item one by one until the target is found.
# Example: Search Student ID
# Time complexity: O(n)
# '''
# student_ids = [101, 102, 103, 104, 105]

# target = 104

# for index in range(len(student_ids)):
#     if student_ids[index] == target:
#         print("Found at position", index)
#         break

# '''
# 2. Binary Search
# Definition:
# Binary Search repeatedly divides a sorted list into halves.
# Requirement:
# Data must already be sorted.
# Time complexity: O(log n)
# '''
# numbers = [10, 20, 30, 40, 50, 60]

# target = 40

# left = 0
# right = len(numbers) - 1

# while left <= right:
#     mid = (left + right) // 2

#     if numbers[mid] == target:
#         print("Found at index", mid)
#         break
#     elif target < numbers[mid]:
#         right = mid - 1
#     else:
#         left = mid + 1

# '''
# 3. Bubble Sort
# Definition:
# Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.
# Complexity: O(n²)
# '''
# numbers = [5, 3, 8, 1, 2]

# n = len(numbers)

# for i in range(n):
#     for j in range(0, n-i-1):
#         if numbers[j] > numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# print(numbers)

# '''
# 4. Selection Sort
# Definition:
# Selection Sort repeatedly selects the smallest element and places it at the correct position.
# Complexity: O(n²)
# '''
# numbers = [64, 25, 12, 22, 11]

# for i in range(len(numbers)):
#     min_index = i

#     for j in range(i+1, len(numbers)):
#         if numbers[j] < numbers[min_index]:
#             min_index = j

#     numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# print(numbers)

# '''
# 5. Python sort()
# Definition:
# Python provides a built-in sorting method that is faster than Bubble Sort and Selection Sort.
# Example: Sort Employee Names
# Time complexity: O(n log n)
# '''
# employees = ["John", "Mary", "David", "Alice"]

# employees.sort()

# print(employees)

# '''
# Descending order
# '''
# employees.sort(reverse=True)
# '''
# Practical Exercise: Find Maximum and Minimum 
# Problem Statement
# Find both maximum and minimum values in a list.
# Solution
# '''
# numbers = [25, 8, 45, 10, 90, 3]

# maximum = max(numbers)
# minimum = min(numbers)

# print("Maximum:", maximum)
# print("Minimum:", minimum)

# '''
# Hands-On Lab Exercises
# Exercise 1
# Create a text file and write five employee names into it.
# Exercise 2
# Read the file and display all employee names.
# Exercise 3
# Append two new employee names to the file.
# Exercise 4
# Count the total words in a paragraph.
# Exercise 5
# Find duplicate numbers in a list.
# Exercise 6
# Search for a student ID using Linear Search.
# Exercise 7
# Sort a list of employee names using:

# Bubble Sort
# Selection Sort
# Python sort()

# Exercise 8
# Find maximum and minimum values in a list.
# '''
