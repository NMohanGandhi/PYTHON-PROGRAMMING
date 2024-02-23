 # Task1
 ## In XYZ country there is rule that car’s engine no. depends upon car’ number plate. Engine no is sum of all the integers present on car’s Number plate.The issuing authority has hired you in order to provide engine no. to the cars.Your task is to develop an algorithm which takes input as in form of string(Number plate) and gives back

# Engine number.

# Input Description:
## You are given a string ’s’

# Output Description:
## Print the engine number

# Sample Input :
## HR05-AA-2669
# Sample Output :
## 28

### 
<details>
# <summary> Click to view solution</summary>
def calculate_engine_number(s):
    engine_number = 0
    for char in s:
        if char.isdigit():
            engine_number += int(char)
    return engine_number

# Sample Input
s = "HR05-AA-2669"

# Calculate engine number
engine_number = calculate_engine_number(s)

# Output engine number
print(engine_number)
</details>
