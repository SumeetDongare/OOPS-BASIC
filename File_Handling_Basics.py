
#1. Text File
file = open("demo.txt", "r")
print(file.read())
file.close()

#Output: Hello Python

file = open("demo.txt", "w")
file.write("Hello Python")
file.close()
print("Data written successfully")

#Output:Data written successfully

file = open("demo.txt", "a")
file.write("\nWelcome to Python")
file.close()
print("Data appended successfully")

"""Output:Data appended successfully

File content:

Hello Python
Welcome to Python
4. Text File — r+ Read + Write
file = open("demo.txt", "r+")"""


print(file.read())
file.write("\nNew Line")
file.close()

"""Output:
Hello Python
Welcome to Python
"""

# 2 — CSV FILE
import csv
file = open("student.csv", "r")
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()

"""Output:

['Name', 'Age']
['Rahul', '20']
['Amit', '21']
"""

file = open("student.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Name", "Age"])
writer.writerow(["Rahul", 20])
writer.writerow(["Amit", 21])
file.close()
print("CSV file written successfully")

"""Output:

CSV file written successfully

File content:

Name,Age
Rahul,20
Amit,21
9. CSV File — a Append Mode"""

file = open("student.csv", "a", newline="")
writer = csv.writer(file)
writer.writerow(["Suresh", 22])
file.close()
print("Data appended successfully")

"""Output:
Data appended successfully
File content:
Name,Age
Rahul,20
Amit,21
Suresh,22"""

file = open("student.csv", "r+")
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()

"""Output:

['Name', 'Age']
['Rahul', '20']
['Amit', '21']
['Suresh', '22']
"""

# 3 — JSON FILE
import json
file = open("student.json", "r")
data = json.load(file)
print(data)
file.close()

"""Output:

{'name': 'Rahul', 'age': 20}"""

data = {
    "name": "Rahul",
    "age": 20
}

file = open("student.json", "w")
json.dump(data, file)
file.close()
print("JSON file written successfully")

"""Output:

JSON file written successfully

File content:

{"name": "Rahul", "age": 20}"""

file = open("student.json", "r")
data = json.load(file)
file.close()
data["city"] = "Pune"
file = open("student.json", "w")
json.dump(data, file)
file.close()
print("Data added successfully")

"""Output:

Data added successfully

File content:

{"name": "Rahul", "age": 20, "city": "Pune"}"""

# 4- XML File 
import xml.etree.ElementTree as ET
root = ET.Element("student")
name = ET.SubElement(root, "name")
name.text = "Rahul"
age = ET.SubElement(root, "age")
age.text = "20"
tree = ET.ElementTree(root)
file = open("student.xml", "w")
tree.write(file)
file.close()
print("XML file written successfully")

"""Output:

XML file written successfully

File content:

<student>
    <name>Rahul</name>
    <age>20</age>
</student>"""

tree = ET.parse("student.xml")
root = tree.getroot()
city = ET.SubElement(root, "city")
city.text = "Pune"
tree.write("student.xml")
print("Data added successfully")

"""Output:

Data added successfully

File content:

<student>
    <name>Rahul</name>
    <age>20</age>
    <city>Pune</city>
</student>"""

file = open("student.xml", "r+")
tree = ET.parse(file)
root = tree.getroot()
print(root.find("name").text)
age = root.find("age")
age.text = "21"
file.seek(0)
tree.write(file)
file.truncate()
file.close()

"""Output:

Rahul

Updated file:

<student>
    <name>Rahul</name>
    <age>21</age>
    <city>Pune</city>
</student>"""

root = ET.Element("student")
name = ET.SubElement(root, "name")
name.text = "Amit"
age = ET.SubElement(root, "age")
age.text = "21"
tree = ET.ElementTree(root)
file = open("student.xml", "w+")
tree.write(file)
file.seek(0)
tree = ET.parse(file)
root = tree.getroot()
print(root.find("name").text)
print(root.find("age").text)
file.close()
"""
Output:

Amit
21"""

file = open("student.xml", "a+")
file.seek(0)
tree = ET.parse(file)
root = tree.getroot()
course = ET.SubElement(root, "course")
course.text = "Python"
file.seek(0)
tree.write(file)
file.truncate()
file.close()
print("XML updated successfully")

"""Output:

XML updated successfully

File content:

<student>
    <name>Amit</name>
    <age>21</age>
    <course>Python</course>
</student>"""
