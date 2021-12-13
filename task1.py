"""Algorithm Structure Used
    Input fields: Name and Age
    Expected Output: so you are {Name} and {Age} years old. Nice to meet
    Ask for name
    Ask for age
    Validate age as a number
    Output
"""

print("Hello how are you doing??\n")

condition = True
while condition:
    name = input("can I please know your name?\n")
    age = input("can I please know your age?\n")

    if name.isalpha() & age.isdigit():
        output = f"\nso you are {name} and you're {age} years old. Nice to meet you"
        print(output)
        condition = False
    else:
        print("Invalid name Or Age, Please pass in a number for the age and letter only for the name\n")