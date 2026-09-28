'''
What is YAML?
YAML (YAML Ain't Markup Language) is a human-readable format used to store configuration and settings data.
Think of YAML as a cleaner and more readable alternative to XML and sometimes JSON.
Real-World Uses

Application Configuration Files
Docker Compose
Kubernetes
CI/CD Pipelines (GitHub Actions, Jenkins, Azure DevOps)
Infrastructure as Code


Why Use YAML?
JSON
{
  "application": {
    "name": "InventoryApp",
    "version": "1.0"
  }
}
YAML
application:
  name: InventoryApp
  version: 1.0

Notice how YAML is easier to read because:

No curly braces { }
No square brackets [ ]
No commas
Uses indentation


YAML Basics
YAML stores data as:
1. Key-Value Pairs
Similar to Python dictionaries.
name: John
age: 25
city: Chennai

Equivalent Python:
{
    "name": "John",
    "age": 25,
    "city": "Chennai"
}


2. Lists
Lists use a hyphen (-).
YAML
skills:
  - Python
  - SQL
  - Azure

Python
{
    "skills": [
        "Python",
        "SQL",
        "Azure"
    ]
}

3. Nested Objects
YAML uses indentation for hierarchy.
YAML
employee:
  id: 101
  name: John
Python
{
    "employee": {
        "id": 101,
        "name": "John"
    }
}

YAML Data Types
YAML supports similar data types as JSON.

String
name: John
city: Chennai
Python:
str

Number
age: 25
salary: 75000.50

Python:
int
float

Boolean
is_active: true
is_active: false
Python:
True
False

Null
manager: null
or
manager:
Python:
None

List
skills:
  - Python
  - SQL
Python:
list

Dictionary (Object)
employee:
  name: John
  department: IT
Python:
dict

Indentation is Very Important
Unlike Python, YAML does not use braces.
Indentation defines structure.
✅ Correct
employee:
  id: 101
  name: John
❌ Wrong
employee:
id: 101
name: John
This causes parsing errors.

Complete YAML Example
employee:
  id: 101
  name: John Smith
  department: IT
  salary: 75000

skills:
  - Python
  - SQL
  - Azure

address:
  city: Chennai
  country: India
Equivalent Python:
{
    "employee": {
        "id": 101,
        "name": "John Smith",
        "department": "IT",
        "salary": 75000
    },
    "skills": [
        "Python",
        "SQL",
        "Azure"
    ],
    "address": {
        "city": "Chennai",
        "country": "India"
    }
}
Installing PyYAML
PyYAML is the most commonly used Python library for YAML.
Shell
pip install pyyaml


YAML Comments
One advantage of YAML over JSON is comments.
YAML
# Database configuration
 database:  
   host: localhost  
   port: 3306
JSON does not support comments.

YAML Lists of Objects
Very common in real projects.
employees:
  - id: 101
    name: John

  - id: 102
    name: Mary

Python Representation:
{
    "employees": [
        {
            "id": 101,
            "name": "John"
        },
        {
            "id": 102,
            "name": "Mary"
        }
    ]
}
Access first employee:
Pythondata["employees"][0]["name"]
Output:
John

Real-Time Example: Docker Compose
version: "3"

services:
  web:
    image: nginx
    ports:
      - "80:80"
This YAML file tells Docker:

Use image nginx
Run a web service
Map port 80

This is why YAML is heavily used in DevOps.

Interview Questions
What is YAML?
A human-readable data serialization language commonly used for configuration files.

Why is YAML popular?

Easy to read
Easy to write
Supports nesting
Used in DevOps tools


Which Python library is commonly used for YAML?
PythonPyYAMLShow more lines

Which function should be used to read YAML safely?
yaml.safe_load()

What does yaml.dump() do?
Converts Python objects into YAML format and writes them to a file or stream.

'''