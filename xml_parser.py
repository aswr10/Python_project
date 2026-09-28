
'''
XML Structure
What is XML?

XML (eXtensible Markup Language) is used to store and transport data in a structured format.

Sample XML
<?xml version="1.0"?>
<employees>
    <employee>
        <id>101</id>
        <name>John</name>
        <department>IT</department>
        <salary>50000</salary>
    </employee>

    <employee>
        <id>102</id>
        <name>Mary</name>
        <department>HR</department>
        <salary>45000</salary>
    </employee>
</employees>

XML Components
Component	Example
Root Element	employees
Child Element	employee
Tag	            name
Value	        John
Attribute	    id="101"


ElementTree Module

Python provides the built-in xml.etree.ElementTree module.
Import Module

import xml.etree.ElementTree as ET

Common Functions
Function	    Purpose
ET.parse()	    Parse XML file
getroot()	    Get root element
find()	        Find first matching element
findall()	    Find all matching elements
SubElement()	Create child element
write()	        Save XML file

Read XML File
employee.xml

<employees>
    <employee>
        <id>101</id>
        <name>John</name>
        <department>IT</department>
    </employee>

    <employee>
        <id>102</id>
        <name>Mary</name>
        <department>HR</department>
    </employee>
</employees>

'''
# import xml.etree.ElementTree as ET

# tree = ET.parse("employee.xml")
# root = tree.getroot()

# print(root.tag)

'''
Extract Values from XML
Extract All Employee Details
'''
# import xml.etree.ElementTree as ET

# tree = ET.parse("employee.xml")
# root = tree.getroot()

# for emp in root.findall("employee"):
#     emp_id = emp.find("id").text
#     name = emp.find("name").text
#     dept = emp.find("department").text

#     print(emp_id, name, dept)

'''
Practical Exercise 1: Read Employee XML
Problem Statement

Read an employee XML file and display all employee information.

Solution
'''
# import xml.etree.ElementTree as ET

# tree = ET.parse("employee.xml")
# root = tree.getroot()

# for employee in root.findall("employee"):
#     print("ID:", employee.find("id").text)
#     print("Name:", employee.find("name").text)
#     print("Department:", employee.find("department").text)
#     print("-" * 20)

'''
Practical Exercise 2: Extract Employee Names
Problem Statement

Display only employee names from XML.

Solution
'''
# import xml.etree.ElementTree as ET

# tree = ET.parse("employee.xml")
# root = tree.getroot()

# for employee in root.findall("employee"):
#     print(employee.find("name").text)

'''
Practical Exercise 3: Convert XML Data to Dictionary
Problem Statement

Convert employee XML data into Python dictionaries.

Solution
'''
# import xml.etree.ElementTree as ET

# tree = ET.parse("employee.xml")
# root = tree.getroot()

# employees = []

# for emp in root.findall("employee"):
#     employees.append({
#         "id": emp.find("id").text,
#         "name": emp.find("name").text,
#         "department": emp.find("department").text
#     })

# print(employees)

'''
Create XML Files
Create Employee XML
'''
# import xml.etree.ElementTree as ET

# root = ET.Element("employees")

# employee = ET.SubElement(root, "employee")

# ET.SubElement(employee, "id").text = "101"
# ET.SubElement(employee, "name").text = "John"
# ET.SubElement(employee, "department").text = "IT"

# tree = ET.ElementTree(root)

# tree.write("new_employee.xml")
'''
Hands-on Activity

Create an XML file for:

Employee ID : 201
Name : David
Department : Finance
Salary : 65000

Expected Output:

<employee>
    <id>201</id>
    <name>David</name>
    <department>Finance</department>
    <salary>65000</salary>
</employee>

XML Assignment
Task

Create a student.xml file containing:

Student ID
Student Name
Course
Marks

Then:

Read the XML file
Display all students
Extract only student names
Convert XML to dictionary

'''
