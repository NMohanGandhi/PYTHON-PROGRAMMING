**The most commonly used object in any project and in any programming language is String only. Hence we should aware complete information about String data type.**

# What is String?
**Any sequence of characters within either single quotes or double quotes is considered as a
String.**

# Task1

In XYZ country, there is a rule that a car’s engine number depends upon the car’s number plate. The engine number is the sum of all the integers present on the car’s number plate. The issuing authority has hired you to provide the engine number to the cars. Your task is to develop an algorithm which takes input in the form of a string (Number plate) and gives back the Engine number.

**Input Description:**  
You are given a string ’s’

**Output Description:**  
Print the engine number

**Sample Input :**  
HR05-AA-2669

**Sample Output :**  
28

```python
def calculate_engine_number(s):
    engine_number = 0
    for char in s:
        if char.isdigit():
            engine_number += int(char)
    return engine_number

s = "HR05-AA-2669"
engine_number = calculate_engine_number(s)
print(engine_number) 
```
# Task2

Rahul is given a task to manipulate a string, He hired you as a developer your task is to delete all the repeating characters and print the result left.

**Input Description:**
You are given a string ‘s’

**Output Description:**
Print the remaining string

**Sample Input :**
mississipie
**Sample Output :**
mpe
 
```python
s = input()

count = {}
for i in s:
    count[i] = s.count(i)
    
final = ''.join(i for i,j in count.items() if j <= 1)
print(final)
```
**Method-2**

```python
s = input()

unique_chars = []
seen_chars = set()

for char in s:
    if char not in seen_chars:
        unique_chars.append(char)
        seen_chars.add(char)

final = ''.join(unique_chars)
print(final)
```


