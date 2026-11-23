# 100 Days of Code – Python
## Day 1: Python Basics

**Topics Covered:**
1. What is Python?
2. Printing
3. Commenting
4. Debugging
5. String Manipulation
6. Variables
7. Variable Naming Rules

---

# 1. What is Python?

Python is a high-level, general-purpose programming language.

It is known for its simple and readable syntax, which makes it suitable for beginners.

Python is used in many areas, such as:

- Automation
- Web development
- Data analysis
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Software testing
- Embedded testing and test automation

### Why is Python easy to learn?

Python syntax is similar to simple English.

For example, to display a message:

```python
print("Hello World")
```

We do not need to write complicated instructions to display text.

### What is a programming language?

A programming language is a language used to communicate instructions to a computer.

For example:

```python
print("Start the vehicle")
```

This instruction tells Python to display the message:

```text
Start the vehicle
```

### What is an interpreter?

Python is commonly executed using an interpreter.

The Python interpreter reads and executes Python instructions.

When we run:

```python
print("Hello")
```

The Python interpreter executes the instruction and displays the output.

---

# 2. Printing in Python

The `print()` function is used to display information on the screen.

### Syntax

```python
print(value)
```

Here, `value` can be:

- Text
- A number
- A variable
- The result of an expression

### Example 1: Printing text

```python
print("Hello Python")
```

Output:

```text
Hello Python
```

### Example 2: Printing numbers

```python
print(10)
print(25.5)
```

Output:

```text
10
25.5
```

Notice that numbers do not require quotation marks.

### Example 3: Printing multiple values

```python
print("Python", "is", "easy")
```

Output:

```text
Python is easy
```

By default, `print()` separates multiple values using a space.

### Example 4: Printing multiple lines

```python
print("Hello")
print("Welcome to Python")
print("Day 1 completed")
```

Output:

```text
Hello
Welcome to Python
Day 1 completed
```

Each `print()` statement normally moves the cursor to a new line.

### Example 5: Using `sep`

The `sep` parameter specifies the separator between multiple values.

```python
print("2026", "11", "22", sep="-")
```

Output:

```text
2026-11-22
```

### Example 6: Using `end`

By default, `print()` ends with a newline.

We can change this using the `end` parameter.

```python
print("Hello", end=" ")
print("Python")
```

Output:

```text
Hello Python
```

### Important points

- `print()` displays information.
- Text is written inside quotation marks.
- Numbers can be printed without quotation marks.
- Multiple values can be printed together.
- `sep` changes the separator.
- `end` changes what is printed at the end.

---

# 3. Commenting in Python

A comment is text written in the program to explain the code.

Python ignores comments during normal execution.

Comments help programmers understand:

- What the code does
- Why a particular instruction is used
- Important logic
- Temporary debugging information

## 3.1 Single-line comments

A single-line comment begins with the `#` symbol.

### Example

```python
# This is a comment

print("Hello Python")
```

Output:

```text
Hello Python
```

The comment is not displayed in the output.

### Example: Comment explaining code

```python
# Display the welcome message
print("Welcome to Python")
```

Output:

```text
Welcome to Python
```

## 3.2 Comments after code

We can also write a comment on the same line as a statement.

```python
print("Hello")  # Display a greeting
```

Output:

```text
Hello
```

## 3.3 Multiple-line comments

Python does not have a special multiline-comment symbol.

We can write multiple comments using `#`.

```python
# This program displays a welcome message.
# It is written as part of Day 1.
# The print function displays text.

print("Welcome to Python")
```

## 3.4 Docstrings

Triple quotes are commonly used to write documentation strings, called docstrings.

They are often used to describe functions, classes, and modules.

```python
def greet():
    """This function displays a greeting."""
    print("Hello")
```

A docstring is different from an ordinary comment. Python stores it as documentation for the function.

### Important points

- `#` is used for ordinary comments.
- Comments improve readability.
- Python ignores ordinary comments during execution.
- Comments should explain useful information.
- Avoid writing unnecessary comments for obvious code.

---

# 4. Debugging in Python

Debugging is the process of finding and fixing errors in a program.

A mistake in a program is called a bug.

For example:

```python
print("Hello Python"
```

Output:

```text
SyntaxError: '(' was never closed
```

The closing parenthesis is missing.

Correct code:

```python
print("Hello Python")
```

Output:

```text
Hello Python
```

## 4.1 Common types of errors

### A. Syntax Error

A syntax error occurs when the code does not follow Python's grammar rules.

Example:

```python
print("Hello"
```

Problem: Missing closing parenthesis.

Correct:

```python
print("Hello")
```

### B. Name Error

A name error occurs when Python cannot find a name that is being used.

Example:

```python
print(message)
```

Output:

```text
NameError: name 'message' is not defined
```

Problem: The variable `message` has not been created.

Correct:

```python
message = "Hello Python"
print(message)
```

### C. Logic Error

A logic error occurs when the program runs without an error but produces an incorrect result.

Example:

```python
length = 10
width = 5

area = length + width

print(area)
```

Output:

```text
15
```

Problem: The area of a rectangle should be calculated using multiplication.

Correct:

```python
length = 10
width = 5

area = length * width

print(area)
```

Output:

```text
50
```

## 4.2 How to debug a program

1. Run the program.
2. Read the error message.
3. Identify the line where the error occurred.
4. Check spelling, syntax, and logic.
5. Correct the mistake.
6. Run the program again.

### Debugging example

Incorrect code:

```python
name = "Ashina"

print(nam)
```

Problem: The variable name is `name`, but we used `nam`.

Correct code:

```python
name = "Ashina"

print(name)
```

Output:

```text
Ashina
```

### Important points

- Debugging helps us find and fix errors.
- Error messages provide useful information.
- Syntax errors are usually easy to identify.
- Logic errors require checking the program's behavior.
- Debugging is an important skill for every programmer.

---

# 5. String Manipulation

A string is a sequence of characters.

Characters can include:

- Letters
- Numbers
- Spaces
- Symbols

In Python, strings are written inside quotation marks.

### Examples

```python
name = "Ashina"
message = 'Hello Python'
number_as_text = "123"
```

Notice that `"123"` is a string because it is inside quotation marks.

## 5.1 Single and double quotes

Both single and double quotes can be used to create strings.

```python
name = "Ashina"
city = 'Bengaluru'

print(name)
print(city)
```

Output:

```text
Ashina
Bengaluru
```

## 5.2 String concatenation

String concatenation means joining strings together.

We use the `+` operator.

```python
first_name = "Ashina"
last_name = "V"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Ashina V
```

Here:

- `first_name` contains `"Ashina"`
- `" "` contains one space
- `last_name` contains `"V"`

The `+` operator joins these strings.

## 5.3 String repetition

The `*` operator can repeat a string.

```python
print("Python " * 3)
```

Output:

```text
Python Python Python
```

## 5.4 String length

The `len()` function returns the number of characters in a string.

```python
name = "Python"

print(len(name))
```

Output:

```text
6
```

Spaces are also counted as characters.

```python
message = "Hello Python"

print(len(message))
```

Output:

```text
12
```

## 5.5 String indexing

Indexing means accessing an individual character from a string.

Python indexing starts from `0`.

```python
name = "Python"

print(name[0])
print(name[1])
print(name[2])
```

Output:

```text
P
y
t
```

Index positions:

| Character | Index |
|---|---|
| P | 0 |
| y | 1 |
| t | 2 |
| h | 3 |
| o | 4 |
| n | 5 |

We can also use negative indexing.

```python
name = "Python"

print(name[-1])
```

Output:

```text
n
```

`-1` refers to the last character.

## 5.6 String slicing

Slicing is used to extract a part of a string.

Syntax:

```python
string[start:stop]
```

The starting index is included, but the stopping index is excluded.

Example:

```python
name = "Python"

print(name[0:3])
```

Output:

```text
Pyt
```

Explanation:

- Start index = 0
- Stop index = 3
- Characters at indexes 0, 1, and 2 are selected

## 5.7 Escape characters

Escape characters allow us to represent special characters inside strings.

### Newline

```python
print("Hello\nPython")
```

Output:

```text
Hello
Python
```

`\n` moves the text to a new line.

### Tab

```python
print("Hello\tPython")
```

Output:

```text
Hello    Python
```

`\t` inserts a tab space.

### Quotation marks inside a string

```python
print("Python is called \"easy\"")
```

Output:

```text
Python is called "easy"
```

The backslash allows the quotation mark to be included inside the string.

## 5.8 String immutability

Strings in Python are immutable.

This means we cannot directly change an individual character in an existing string.

Incorrect:

```python
name = "Python"

name[0] = "J"
```

This produces a `TypeError`.

Correct:

```python
name = "Python"

name = "J" + name[1:]

print(name)
```

Output:

```text
Jython
```

Here, we create a new string and assign it to the variable `name`.

---

# 6. Variables in Python

A variable is a name used to refer to a value.

Variables help us store and reuse information.

### Example

```python
name = "Ashina"
age = 27

print(name)
print(age)
```

Output:

```text
Ashina
27
```

Here:

- `name` refers to the string `"Ashina"`.
- `age` refers to the integer `27`.

## 6.1 Variable assignment

The `=` operator is used for assignment.

```python
number = 10
```

This means:

Assign the value `10` to the variable `number`.

It does not mean that `number` is mathematically equal to 10 in an equation.

## 6.2 Changing a variable value

```python
number = 10

print(number)

number = 20

print(number)
```

Output:

```text
10
20
```

The variable now refers to the new value.

## 6.3 Assigning multiple variables

```python
a = 10
b = 20
c = 30

print(a)
print(b)
print(c)
```

We can also assign multiple variables in one line.

```python
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)
```

Output:

```text
10
20
30
```

## 6.4 Using variables in calculations

```python
length = 10
width = 5

area = length * width

print(area)
```

Output:

```text
50
```

Variables make programs easier to modify.

If the length changes, we only need to update the variable.

## 6.5 Variables can store different data types

```python
name = "Ashina"       # String
age = 27              # Integer
height = 167.5        # Float
is_learning = True    # Boolean
```

Python automatically determines the data type based on the assigned value.

We will study data types in more detail in a later lesson.

---

# 7. Variable Naming Rules

Variable names should be meaningful and follow Python's naming rules.

## 7.1 Rules for naming variables

### Rule 1: A variable name must begin with a letter or underscore

Valid:

```python
name = "Ashina"
_age = 27
```

Invalid:

```python
2name = "Ashina"
```

A variable name cannot begin with a number.

### Rule 2: Variable names can contain letters, numbers, and underscores

Valid:

```python
user_name = "Ashina"
age2 = 27
vehicle_speed = 80
```

Invalid:

```python
user-name = "Ashina"
```

A hyphen is not allowed in a variable name.

### Rule 3: Spaces are not allowed

Invalid:

```python
user name = "Ashina"
```

Correct:

```python
user_name = "Ashina"
```

### Rule 4: Python is case-sensitive

```python
name = "Ashina"
Name = "Python"

print(name)
print(Name)
```

Output:

```text
Ashina
Python
```

`name` and `Name` are two different variables.

### Rule 5: Do not use Python keywords as variable names

Keywords are reserved words that have special meanings in Python.

Examples:

- `if`
- `else`
- `for`
- `while`
- `class`
- `def`
- `True`
- `False`

Invalid:

```python
if = 10
```

Correct:

```python
condition = 10
```

## 7.2 Recommended naming style

Python commonly uses **snake_case** for variable names.

In snake_case, words are separated using underscores.

Examples:

```python
first_name = "Ashina"
vehicle_speed = 80
engine_temperature = 95
battery_voltage = 12.5
```

Avoid unclear variable names.

Poor naming:

```python
x = 100
y = 200
z = 300
```

Better naming:

```python
vehicle_speed = 100
engine_temperature = 200
battery_voltage = 300
```

Meaningful variable names improve code readability.

---

# 8. Complete Day 1 Example Program

This program combines the concepts learned today.

```python
# Day 1 - Python Basics
# This program displays basic vehicle information.

# Store vehicle information in variables
vehicle_name = "Smart Vehicle"
vehicle_speed = 60
engine_temperature = 85.5

# Calculate the speed after increasing it
new_speed = vehicle_speed + 10

# Display vehicle information
print("Vehicle Name:", vehicle_name)
print("Current Speed:", vehicle_speed, "km/h")
print("Engine Temperature:", engine_temperature, "°C")

# Display the updated speed
print("Updated Speed:", new_speed, "km/h")

# Display a message using string concatenation
message = "Welcome to " + vehicle_name

print(message)
```

Output:

```text
Vehicle Name: Smart Vehicle
Current Speed: 60 km/h
Engine Temperature: 85.5 °C
Updated Speed: 70 km/h
Welcome to Smart Vehicle
```

### What did we use in this program?

- Comments to explain the program
- Variables to store information
- Strings to store text
- Numbers to store speed and temperature
- `print()` to display information
- `+` to perform addition and string concatenation

This is a simple example of how Python can be used in automotive-related applications.

---

# 9. Day 1 Quick Revision

| Concept | Meaning |
|---|---|
| Python | A high-level programming language |
| `print()` | Displays information |
| `#` | Starts an ordinary comment |
| Debugging | Finding and fixing errors |
| String | A sequence of characters |
| Concatenation | Joining strings |
| `len()` | Returns the length of a string |
| Indexing | Accessing a character |
| Slicing | Extracting part of a string |
| Variable | A name referring to a value |
| `=` | Assignment operator |
| Snake case | Naming style using underscores |

---

# 10. Day 1 Practice Questions

Try to solve these without looking at the examples.

### Question 1
Write a Python program to print:

```text
Hello
I am learning Python
Day 1 completed
```

### Question 2
Create variables for:

- Your name
- Your age
- Your current learning topic

Print all three values.

### Question 3
Write a program to join your first name and last name using string concatenation.

### Question 4
Find the length of the string:

```python
message = "Python Programming"
```

### Question 5
Print the first and last characters of:

```python
language = "Python"
```

### Question 6
Identify the error:

```python
2name = "Python"
print(2name)
```

### Question 7
What is the output?

```python
a = 10
b = 20

print(a + b)
print(a * b)
```

### Question 8
Correct the logic error:

```python
length = 10
width = 5

area = length + width

print(area)
```

### Question 9
Write a program with at least three comments explaining what the code does.

### Question 10
Create a variable named `vehicle_speed`, assign it a value of 80, and print:

```text
Vehicle speed is 80 km/h
```

---

**Day 1 Status: Completed**

You have learned the basic building blocks of Python. These concepts will be used in the next lessons when we study data types, mathematical operations, and user input.