'''
Excel Processing

Excel Libraries
Pandas

Most popular library for Excel processing.

Installation

pip install pandas openpyxl


pip install numpy-*.whl
pip install six-*.whl
pip install python_dateutil-*.whl
pip install pytz-*.whl
pip install tzdata-*.whl
pip install et_xmlfile-*.whl
pip install openpyxl-*.whl
pip install pandas-*.whl


Import
import pandas as pd

Read Excel File
employees.xlsx


'''

# import pandas as pd

# df = pd.read_excel("employees.xlsx")

# print(df)

'''
1. What is a DataFrame?

A DataFrame is a 2-dimensional table in Pandas, similar to an Excel sheet.

With index=False
df.to_excel("report.xlsx", index=False)

Excel output:
Name    Salary
John    50000
Mary    45000

The index column is not saved.

This is usually what we want for reports.

With index=True (default)

Excel output:
    Name    Salary
0   John    50000
1   Mary    45000
Write Excel File
Create Excel Report
'''

# import pandas as pd

# data = {
#     "Name": ["John", "Mary"],
#     "Salary": [50000, 45000]
# }

# df = pd.DataFrame(data)

# df.to_excel("report.xlsx", index=False)

'''
Filtering Data
Employees with Salary > 50000
'''
# import pandas as pd

# df = pd.read_excel("employees.xlsx")

# result = df[df["Salary"] > 50000]

# print(result)
'''
Grouping Data
What does mean() do?

mean() calculates the average.
Group By Department
'''
# import pandas as pd

# df = pd.read_excel("employees.xlsx")

# grouped = df.groupby("Department")["Salary"].mean()

# print(grouped)

'''
Practical Exercise 1: Employee Report Generation
Problem Statement

Generate employee salary report.

Solution
'''
# import pandas as pd

# df = pd.read_excel("employees.xlsx")

# report = df[["Name", "Department", "Salary"]]

# report.to_excel("employee_report.xlsx", index=False)

# print("Report Generated")

'''
Practical Exercise 2: Sales Summary Report
sales.xlsx
'''
# import pandas as pd

# df = pd.read_excel("sales.xlsx")

# summary = df.groupby("Product")["Sales"].sum()

# print(summary)

'''
Practical Exercise 3: Excel to JSON Conversion
Problem Statement

Convert Excel file to JSON.
'''

# import pandas as pd

# df = pd.read_excel("employees.xlsx")

# json_data = df.to_json(
#     orient="records",
#     indent=4
# )

# print(json_data)

'''
Mini Project: Employee Management Data Processing
Requirements
Part 1 – XML
Read employee XML
Extract employee names
Convert XML to dictionary
Part 2 – Excel
Read employee Excel
Generate report
Filter salary > 50000
Group by department
Export results to Excel
Convert final report to JSON
Assessment Questions
XML
What is XML?
What is a root node?
Difference between find() and findall()?
How to read an XML file?
How to create XML using ElementTree?
Excel
What is Pandas?
How do you read an Excel file?
How do you write data to Excel?
What is filtering?
What is grouping?
How do you convert Excel to JSON?
'''