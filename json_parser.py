'''
Module 1: JSON Processing

JSON Basics
Read JSON
Write JSON

Module 2: YAML Parsing

YAML Structure
PyYAML Library
Read YAML
Write YAML

Prerequisites

Python fundamentals
Dictionaries and Lists in Python
File handling basics
'''
'''
Module 1: JSON Processing
1. JSON Basics
What is JSON?
JSON (JavaScript Object Notation) is a lightweight data interchange format 
used to exchange data between applications.
JSON Features

Human-readable
Language-independent
Lightweight
Easy to parse and generate

JSON Data Types

JSON Type  Python Equivalent
Object      Dictionary
Array       List
String      str
Number      int/float
Boolean     bool
Null        None

Sample JSON

{    
    "employee_id": 101,    
    "name": "John",    
    "department": "IT",    
    "salary": 70000,    
    "is_active": true
}

Exercise 1: Employee JSON File Creation
Objective
Create a JSON file containing employee details.
'''
#Step 1: Create employee dictionary

# import json

# employee = {    
# "employee_id": 101,    
# "name": "John Smith",    
# "department": "IT",    
# "salary": 75000,    
# "skills": ["Python", "SQL", "Azure"]
# }

# #Step 2: Write to JSON file
# with open("employee.json", "w") as file:    
#     json.dump(employee, file, indent=4)
#     print("Employee JSON file created successfully.")
# '''    
# Generated employee.json
# JSON{    
# "employee_id": 101,    
# "name": "John Smith",    
# "department": "IT",    
# "salary": 75000,    
# "skills": ["Python", "SQL", "Azure"]
# }
# '''

# #Step 2: Write to JSON file
# with open("employee.json", "w") as file:    
#     json.dump(employee, file, indent=4)
#     print("Employee JSON file created successfully.")
# '''    
# Generated employee.json
# JSON{    
# "employee_id": 101,    
# "name": "John Smith",    
# "department": "IT",    
# "salary": 75000,    
# "skills": ["Python", "SQL", "Azure"]
# }
# '''
# '''
# Practice Task
# Create JSON files for:

# Student information
# Product catalog
# Vehicle details
# '''
# """
# 2. Read JSON
# Objective
# Read customer data from a JSON file.
# customer.json
# JSON{   
#      "customer_id": 1001,    
#      "name": "Alice",    
#      "email": "alice@email.com",    
#      "city": "New York"
#      }
# """

# import json
# with open("customer.json", "r") as file:    
#     customer = json.load(file)
#     print("Customer ID:", customer["customer_id"])
#     print("Customer Name:", customer["name"])
#     print("Email:", customer["email"])
#     print("City:", customer["city"])
# '''
# Output
# Plain Text
# Customer ID: 1001
# Customer Name: Alice
# Email: alice@email.com
# City: New York
# '''
# #Reading JSON String
# import json
# json_string = '''
# {    
#   "name":"Tom",    
#    "age":25
# }
# '''
# data = json.loads(json_string)
# print(data)
# '''
# Output
# Python{'name': 'Tom', 'age': 25}`
# '''
# '''
# Practice Exercise
# Read a JSON file containing:
# JSON{  
#     "product_id": 501,  
#     "product_name": "Laptop",  
#     "price": 1200}
# Display all values.
# '''


# # 3. Write JSON
# # Objective
# # Convert Python dictionary to JSON.
# # Dictionary Example

# import json
# student = {    
#     "roll_no": 10,    
#     "name": "David",    
#     "course": "Python"
# }
# #Convert to JSON String
# json_data = json.dumps(student, indent=4)
# print(json_data)

# '''
# Output
# JSON{    
#     "roll_no": 10,   
#       "name": "David",    
#       "course": "Python"
#       }
# '''


# #Save Dictionary as JSON
# import json
# student = {    
#     "roll_no": 10,    
#     "name": "David",    
#     "course": "Python"
# }
# with open("student.json", "w") as file:    
#     json.dump(student, file, indent=4)
#     print("JSON file written successfully.")

# '''
# Mini Project
# Employee Management System
# Tasks:

# Create employee records.
# Store in JSON file.
# Read JSON file.
# Update employee salary.
# Save changes back to JSON.

# '''
# """
# Module 2: YAML Parsing

# 1. YAML Structure
# What is YAML?
# YAML (YAML Ain't Markup Language) is a human-friendly configuration file format widely used in:

# DevOps
# Docker
# Kubernetes
# CI/CD pipelines
# Application configurations


# Complete YAML Example
# YAML
# employee:  
#     id: 101
#     name: John
# department:    
#     name: IT  
#     location: Chennai
#     skills:  - Python  - SQL  - Azure
# """
# #2. PyYAML Library
# #Installation
# #Shell
# # pip install pyyaml

# #Import Module
#import yaml

# #Verify Installation
# import yaml
# print(yaml.__version__)

# '''
# 3. Read YAML
# Objective
# Read application configuration.
# config.yaml
# application:  
#     name: InventoryApp  
#     version: 1.0
# database:  
#     host: localhost  
#     port: 3306
# '''
# #Python Code
# import yaml
# with open("config.yaml", "r") as file:   
#     config = yaml.safe_load(file)
#     print(config)

# """
# Output
# Python{
#  'application': 
#  {    
#  'name': 'InventoryApp',    
#  'version': 1.0 
#  }, 
#  'database': 
#  {    
#  'host': 'localhost',    
#  'port': 3306 
#  }}
#  """

# #Access YAML Values
# import yaml
# with open("config.yaml", "r") as file:    
#     config = yaml.safe_load(file)
# print("Application Name:", config["application"]["name"])
# print("Database Host:", config["database"]["host"])

# '''
# Exercise
# Read the following YAML:
# server:  
#     ip: 192.168.1.100  
#     port: 8080
# Display IP and Port.
# '''
# '''
# 4. Write YAML
# Objective
# Update YAML configuration.
# Create Python Dictionary
# '''


# #Write to YAML
# import yaml
# config = {    
#     "application": 
#     {        
#         "name": "InventoryApp",        
#         "version": "2.0"    
#     },    
#     "database": 
#     {        
#         "host": "localhost",        
#         "port": 3306    
#     }
# }
# with open("config.yaml", "w") as file:    
#     yaml.dump(config, file)
#     print("YAML file written successfully.")
    
# '''
# Generated YAML
# YAML
# application:  
# name: InventoryApp  
# version: '2.0'
# database:  
# host: localhost  
# port: 3306
# '''
# #Update YAML Configuration
#Read Existing YAML
# import yaml
# with open("config.yaml", "r") as file:    
#     data = yaml.safe_load(file)
# #Update Data
# data["database"]["host"] = "production-db-server"
# #Save Back
# with open("config.yaml", "w") as file:    
#     yaml.dump(data, file)

# '''
# Output YAML
# YAML
# database:
#     host: production-db-server  
#     port: 3306
# '''

# '''
# Convert YAML to JSON
# YAML File
# YAML
# employee:  
#     id: 101  
#     name: John  
#     department: IT
# '''
# #Python Script

# import yaml
# import json
# with open("employee.yaml", "r") as yaml_file:    
#     yaml_data = yaml.safe_load(yaml_file)
# with open("employee.json", "w") as json_file:    
#     json.dump(yaml_data, json_file, indent=4)
# print("YAML converted to JSON successfully.")

# '''
# Output JSON
# JSON{    
#     "employee": 
#     {        
#     "id": 101,        
#     "name": "John",        
#     "department": "IT"    
#     }}
# '''

# '''
# Hands-On Lab
# Lab 1: JSON

# Create Employee JSON
# Read Employee JSON
# Update Salary
# Add New Skill
# Save Changes

# Lab 2: YAML

# Create app configuration YAML
# Read configuration
# Update database credentials
# Write updated YAML
# Convert YAML to JSON


# Final Assignment
# Build a Configuration Management System that:

# Stores employee data in JSON.
# Stores application settings in YAML.
# Reads both files.
# Updates records/configurations.
# Converts YAML data to JSON.
# Generates a final report.

# '''