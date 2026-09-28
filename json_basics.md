'''
What is JSON?
JSON (JavaScript Object Notation) is a text-based format used to store
and exchange data between systems, applications, APIs, and databases.

Think of JSON as a structured way of representing information.

Real-World Example
Employee information:
{
    "employee_id": 101,
    "name": "John Smith",
    "department": "IT"
}
Instead of storing data in an unstructured sentence:

Employee 101 is John Smith from IT department.
JSON stores it in a structured format that both humans and computers can understand easily.

Why JSON is Popular?
✅ Human-readable

✅ Easy to create and edit

✅ Lightweight

✅ Supported by almost all programming languages

✅ Widely used in REST APIs and web applications

JSON Structure
JSON consists of:

1. Objects
An object is a collection of key-value pairs enclosed in {}.

Example:

{
    "name": "John",
    "age": 25
}
Here:


"name" → key
"John" → value

"age" → key
25 → value

2. Arrays
An array is a collection of values enclosed in [].

Example:

{
    "skills": ["Python", "SQL", "Azure"]
}
JSON Array:

["Python", "SQL", "Azure"]
Similar to Python List:

["Python", "SQL", "Azure"]
JSON Data Types
JSON supports 6 data types.

1. String
A string is text enclosed in double quotes.

JSON

{
    "name": "John"
}
Python

name = "John"
Examples

{
    "city": "Chennai",
    "department": "IT"
}
2. Number
Numbers can be:

Integer
Floating-point
Integer
{
    "age": 25
}
Float

{
    "salary": 85000.50
}
Python Equivalent

age = 25
salary = 85000.50
3. Boolean
Boolean represents True or False.

JSON
{
    "is_active": true
}

{
    "is_active": false
}
Python Equivalent
is_active = True
is_active = False
Important
JSON uses:
true
false
Python uses:
True
False
Notice the capitalization difference.

4. Null
Represents no value or empty value.

JSON

{
    "manager": null
}
Python Equivalent

manager = None
5. Object
A JSON object contains multiple key-value pairs.

JSON
{
    "employee": {
        "id": 101,
        "name": "John"
    }
}
Python Equivalent

employee = {
    "id": 101,
    "name": "John"
}
6. Array
Array stores multiple values.

JSON

{
    "skills": ["Python", "SQL", "Azure"]
}
Python Equivalent

skills = ["Python", "SQL", "Azure"]

JSON Data   Type Mapping
JSON	    Python
String	    str
Number	    int/float
Boolean	    True/False
Null	    None
Object	    dict
Array	    list

Complete Example

{
    "employee_id": 101,
    "name": "John Smith",
    "salary": 75000.50,
    "is_active": true,
    "manager": null,
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

All JSON data types are present here:

Field	     Data Type
employee_id	  Number
name	      String
salary	      Number
is_active	  Boolean
manager	      Null
skills	      Array
address	      Object
Nested        JSON
JSON can contain objects inside objects.

Example:

{
    "employee": {
        "id": 101,
        "name": "John",
        "department": {
            "dept_id": 10,
            "dept_name": "IT"
        }
    }
}
Structure:

employee
 ├── id
 ├── name
 └── department
      ├── dept_id
      └── dept_name
JSON Array of Objects
Very common in real-world APIs.

Example:




JSON
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
Python:
data["employees"][0]["name"]
Output:
John
JSON Rules
Rule 1: Keys must be in double quotes
✅ Correct




JSON
{
    "name": "John"
}
❌ Wrong




JSON
{
    name: "John"
}
Rule 2: Strings must use double quotes
✅ Correct




JSON
{
    "city": "Chennai"
}
❌ Wrong




JSON
{
    "city": 'Chennai'
}
Rule 3: No trailing commas
✅ Correct




JSON
{
    "id": 101,
    "name": "John"
}
❌ Wrong

JSON
{
    "id": 101,
    "name": "John",
}
JSON in Python

Python Dictionary → JSON

import json

employee = {
    "id": 101,
    "name": "John"
}

json_data = json.dumps(employee, indent=4)

print(json_data)
Output:
{
    "id": 101,
    "name": "John"
}
JSON → Python Dictionary

import json

json_string = '''
{
    "id": 101,
    "name": "John"
}
'''

data = json.loads(json_string)

print(type(data))
Output:
<class 'dict'>
Real-Time Example: API Response
When you call a REST API:

{
    "status": "Success",
    "customer": {
        "id": 5001,
        "name": "Alice"
    },
    "orders": [
        {
            "order_id": 101
        },
        {
            "order_id": 102
        }
    ]
}

Access data in Python:

print(data["customer"]["name"])
Output:
Alice

Interview Questions
Q1. What is JSON?
A lightweight data exchange format used to store and transfer structured data.

Q2. What are the JSON data types?
String
Number
Boolean
Null
Object
Array
Q3. Difference between JSON Object and Array?
Object

{
    "name": "John"
}
Stores key-value pairs.

Array

["Python", "SQL", "Azure"]
Stores ordered values.

Q4. Difference between dump() and dumps()?


json.dump()
Writes JSON to a file.


json.dumps()
Converts Python object to a JSON string.

Q5. Difference between load() and loads()?

json.load()
Reads JSON from a file.

json.loads()
Reads JSON from a string.

Quick Memory Trick

Plain Text
JSON = 6 Data Types

S → String
N → Number
B → Boolean
N → Null
O → Object
A → Array


'''