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

<details>
<summary>&#x1f534; solution</summary>

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
</details>
```
