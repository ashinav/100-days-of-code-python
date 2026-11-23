# 100 Days of Code – Python
## Day 3: Conditional Statements, Logical Operators, and Scope

**Topics Covered:**

1. What are conditional statements?
2. Comparison operators
3. `if` statement
4. `if-else` statement
5. `if-elif-else` statement
6. Nested conditional statements
7. Logical operators: `and`, `or`, `not`
8. Code blocks and indentation
9. Scope
10. Local and global variables
11. Namespaces
12. Python's `pass` statement
13. Common mistakes
14. Practice questions

---

# 1. What Are Conditional Statements?

A conditional statement allows a program to make decisions based on a condition.

In real life, we make decisions every day.

For example:

- If it rains, take an umbrella.
- If the temperature is high, switch on the fan.
- If the battery voltage is low, display a warning.
- If the test result is correct, mark the test as PASS.

Python can perform similar decision-making using conditional statements.

### Basic idea

```python
if condition:
    execute_this_code
```

Python checks the condition.

- If the condition is `True`, the code inside the `if` block executes.
- If the condition is `False`, the code inside the `if` block is skipped.

Example:

```python
temperature = 35

if temperature > 30:
    print("Temperature is high")
```

Output:

```text
Temperature is high
```

Explanation:

The condition is:

```python
temperature > 30
```

Since `35 > 30` is `True`, Python executes the `print()` statement.

---

# 2. Comparison Operators

Comparison operators are used to compare two values.

They return either `True` or `False`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `10 == 10` | True |
| `!=` | Not equal to | `10 != 5` | True |
| `>` | Greater than | `10 > 5` | True |
| `<` | Less than | `5 < 10` | True |
| `>=` | Greater than or equal to | `10 >= 10` | True |
| `<=` | Less than or equal to | `5 <= 10` | True |

## 2.1 Equal to (`==`)

```python
a = 10
b = 10

print(a == b)
```

Output:

```text
True
```

Important:

`==` is used to compare values.

`=` is used to assign a value.

```python
a = 10       # Assignment
a == 10      # Comparison
```

## 2.2 Not equal to (`!=`)

```python
a = 10
b = 5

print(a != b)
```

Output:

```text
True
```

Because 10 is not equal to 5.

## 2.3 Greater than (`>`)

```python
speed = 100

print(speed > 80)
```

Output:

```text
True
```

## 2.4 Less than (`<`)

```python
temperature = 25

print(temperature < 30)
```

Output:

```text
True
```

## 2.5 Greater than or equal to (`>=`)

```python
age = 18

print(age >= 18)
```

Output:

```text
True
```

## 2.6 Less than or equal to (`<=`)

```python
voltage = 12

print(voltage <= 15)
```

Output:

```text
True
```

---

# 3. The `if` Statement

The `if` statement executes a block of code only when a condition is true.

### Syntax

```python
if condition:
    statement
```

Example:

```python
age = 20

if age >= 18:
    print("You are eligible")
```

Output:

```text
You are eligible
```

Explanation:

1. Python checks whether `age >= 18`.
2. The condition is `True`.
3. The code inside the `if` block executes.

### Example: Vehicle overspeed warning

```python
vehicle_speed = 100
speed_limit = 80

if vehicle_speed > speed_limit:
    print("Overspeed warning")
```

Output:

```text
Overspeed warning
```

This is an example of decision-making in an automotive application.

---

# 4. The `if-else` Statement

Sometimes we need to execute one block when a condition is true and another block when it is false.

For this, we use `if-else`.

### Syntax

```python
if condition:
    statement_if_true
else:
    statement_if_false
```

Example:

```python
temperature = 25

if temperature > 30:
    print("Temperature is high")
else:
    print("Temperature is normal")
```

Output:

```text
Temperature is normal
```

Explanation:

The condition `temperature > 30` is false.

Therefore, Python executes the `else` block.

## Example: Even or odd number

```python
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

Output:

```text
Odd number
```

Explanation:

The modulus operator `%` returns the remainder.

If a number is divisible by 2, the remainder is 0.

Therefore:

```python
number % 2 == 0
```

checks whether the number is even.

---

# 5. The `if-elif-else` Statement

When we have multiple conditions, we can use `elif`.

`elif` means **else if**.

It allows Python to check another condition when the previous condition is false.

### Syntax

```python
if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
else:
    default_statement
```

Python checks the conditions from top to bottom.

The first condition that evaluates to `True` executes its block.

The remaining conditions are skipped.

## Example: Temperature classification

```python
temperature = 40

if temperature < 20:
    print("Low temperature")
elif temperature < 30:
    print("Normal temperature")
elif temperature < 40:
    print("High temperature")
else:
    print("Very high temperature")
```

Output:

```text
Very high temperature
```

Explanation:

- `temperature < 20` → False
- `temperature < 30` → False
- `temperature < 40` → False
- `else` executes

## Example: Grade calculation

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

Output:

```text
Grade B
```

### Important point

The order of conditions matters.

Consider:

```python
marks = 85

if marks >= 50:
    print("Grade C")
elif marks >= 75:
    print("Grade B")
```

Output:

```text
Grade C
```

Why?

The first condition is already true.

Python does not continue checking the `elif` condition.

Always arrange conditions carefully, usually from the highest or most specific condition to the lowest.

---

# 6. Nested Conditional Statements

A nested conditional statement means placing one conditional statement inside another.

Example:

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a driving license")
else:
    print("You are not eligible")
```

Output:

```text
You can drive
```

Explanation:

1. Python checks whether age is at least 18.
2. Since it is true, Python enters the outer `if` block.
3. It then checks whether the person has a license.
4. Since that condition is true, it displays `"You can drive"`.

### Automotive example

```python
vehicle_speed = 100
engine_running = True

if engine_running:
    if vehicle_speed > 80:
        print("Overspeed warning")
```

Output:

```text
Overspeed warning
```

Nested conditions are useful when one decision depends on another.

---

# 7. Logical Operators

Logical operators are used to combine or modify conditions.

Python has three main logical operators:

- `and`
- `or`
- `not`

## 7.1 The `and` operator

The `and` operator returns `True` only when both conditions are true.

| Condition 1 | Condition 2 | Result |
|---|---|---|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### Example

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")
else:
    print("You cannot drive")
```

Output:

```text
You can drive
```

Both conditions are true.

### Automotive example

```python
vehicle_speed = 100
engine_running = True

if vehicle_speed > 80 and engine_running:
    print("Overspeed warning")
```

The warning is displayed only when:

- Speed is greater than 80.
- Engine is running.

---

## 7.2 The `or` operator

The `or` operator returns `True` when at least one condition is true.

| Condition 1 | Condition 2 | Result |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Example

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")
```

Output:

```text
Weekend
```

Only one condition needs to be true.

### Automotive example

```python
battery_voltage = 10.5
engine_temperature = 110

if battery_voltage < 11 or engine_temperature > 100:
    print("Vehicle warning")
```

Output:

```text
Vehicle warning
```

The warning is displayed if either condition is true.

---

## 7.3 The `not` operator

The `not` operator reverses a Boolean result.

- `not True` becomes `False`.
- `not False` becomes `True`.

Example:

```python
engine_running = False

if not engine_running:
    print("Engine is stopped")
```

Output:

```text
Engine is stopped
```

Explanation:

The value of `engine_running` is `False`.

The `not` operator reverses it to `True`.

Therefore, the `if` block executes.

---

# 8. Code Blocks and Indentation

A code block is a group of statements that belong together.

In Python, indentation is used to define code blocks.

Indentation means adding spaces at the beginning of a line.

Example:

```python
age = 20

if age >= 18:
    print("Eligible")
    print("You can proceed")

print("Program completed")
```

Output:

```text
Eligible
You can proceed
Program completed
```

The first two `print()` statements belong to the `if` block.

The last statement is outside the block.

## Why is indentation important?

Python uses indentation to understand which statements belong to a condition, loop, or function.

Incorrect:

```python
age = 20

if age >= 18:
print("Eligible")
```

This produces an `IndentationError`.

Correct:

```python
age = 20

if age >= 18:
    print("Eligible")
```

### Important rules

- Use consistent indentation.
- Four spaces are the recommended indentation level.
- Statements inside the same block should have the same indentation.
- Do not confuse indentation with ordinary spaces between words.

---

# 9. Scope in Python

Scope refers to the region of a program where a variable can be accessed.

Python commonly uses two scopes when learning functions:

1. Local scope
2. Global scope

## 9.1 Local variables

A local variable is created inside a function.

It is generally accessible only inside that function.

Example:

```python
def greet():
    message = "Hello Python"
    print(message)

greet()
```

Output:

```text
Hello Python
```

Here, `message` is a local variable.

It belongs to the function `greet()`.

Trying to access it outside the function:

```python
def greet():
    message = "Hello Python"

greet()

print(message)
```

This produces a `NameError` because `message` is not defined in the global scope.

## 9.2 Global variables

A global variable is created outside functions.

It can be accessed from functions, provided it is not shadowed by a local variable.

Example:

```python
vehicle_name = "Smart Vehicle"

def display_vehicle():
    print(vehicle_name)

display_vehicle()
```

Output:

```text
Smart Vehicle
```

The variable `vehicle_name` is global because it is defined outside the function.

---

# 10. Local and Global Namespacing

A namespace is a collection of names and the objects they refer to.

For example, a variable name can refer to a value.

```python
name = "Ashina"
age = 27
```

The names `name` and `age` exist in the current namespace.

Python uses namespaces to keep track of variables, functions, and other objects.

## 10.1 Local namespace

A local namespace contains names defined inside a function.

```python
def calculate():
    number = 10
    result = number * 2
    print(result)

calculate()
```

Output:

```text
20
```

Here, `number` and `result` belong to the local namespace of `calculate()`.

## 10.2 Global namespace

The global namespace contains names defined at the module level.

```python
vehicle_speed = 80

def display_speed():
    print(vehicle_speed)

display_speed()
```

Output:

```text
80
```

The variable `vehicle_speed` belongs to the global namespace.

## 10.3 Same variable name in local and global scope

```python
number = 100

def display_number():
    number = 20
    print(number)

display_number()

print(number)
```

Output:

```text
20
100
```

Explanation:

- The global variable `number` contains 100.
- The local variable `number` contains 20.
- Inside the function, Python uses the local variable.
- Outside the function, Python uses the global variable.

The local variable does not change the global variable.

---

# 11. The `global` Keyword

The `global` keyword allows us to modify a global variable from inside a function.

Example:

```python
counter = 0

def increase_counter():
    global counter
    counter = counter + 1

increase_counter()

print(counter)
```

Output:

```text
1
```

Explanation:

Without the `global` keyword, assigning a value to `counter` inside the function would create a local variable.

By using:

```python
global counter
```

we tell Python that we want to use the global variable.

### Important

Using global variables excessively can make programs harder to understand and maintain.

For larger programs, it is often better to pass values to functions and return results.

Example:

```python
def increase_counter(counter):
    return counter + 1

counter = 0
counter = increase_counter(counter)

print(counter)
```

Output:

```text
1
```

This approach avoids modifying a global variable directly.

---

# 12. The `pass` Statement

The `pass` statement is used when Python expects a statement, but we do not want to execute anything yet.

Example:

```python
if True:
    pass
```

This program runs without an error.

The `pass` statement does nothing.

It is useful when creating a function or conditional block that we plan to complete later.

Example:

```python
def check_vehicle_speed():
    pass
```

We can later add the required logic inside the function.

---

# 13. Complete Day 3 Example Program

This program combines conditional statements, logical operators, and variables.

```python
# Day 3 - Conditional Statements
# Simple vehicle safety monitoring example

vehicle_speed = 100
speed_limit = 80

battery_voltage = 12.5
engine_running = True

# Check whether the engine is running
if engine_running:

    # Check vehicle speed
    if vehicle_speed > speed_limit:
        print("Overspeed warning")

    else:
        print("Vehicle speed is normal")

else:
    print("Engine is stopped")

# Check battery voltage
if battery_voltage < 11:
    print("Low battery warning")
else:
    print("Battery voltage is normal")
```

Output:

```text
Overspeed warning
Battery voltage is normal
```

This example demonstrates how Python can make decisions based on vehicle parameters.

---

# 14. Day 3 Quick Revision

| Concept | Meaning |
|---|---|
| `if` | Executes code when a condition is true |
| `else` | Executes when the previous condition is false |
| `elif` | Checks another condition |
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `not` | Reverses a Boolean result |
| Indentation | Defines code blocks |
| Local variable | Defined inside a function |
| Global variable | Defined outside functions |
| Namespace | Collection of names and their objects |
| `global` | Allows assignment to a global variable inside a function |
| `pass` | Does nothing; used as a placeholder |

---

# 15. Day 3 Practice Questions

Try to solve these without looking at the examples.

### Question 1: Positive or negative

Write a program that checks whether a number is positive, negative, or zero.

### Question 2: Even or odd

Write a program that checks whether a number is even or odd.

### Question 3: Compare two numbers

Take two numbers and print the greater number.

### Question 4: Grade calculation

Write a program that displays:

- Grade A for marks 90 or above
- Grade B for marks 75 or above
- Grade C for marks 50 or above
- Fail otherwise

### Question 5: Logical operators

What is the output?

```python
a = 10
b = 20

print(a > 5 and b > 15)
print(a > 15 or b > 15)
print(not(a > 5))
```

### Question 6: Identify the error

```python
age = 20

if age >= 18:
print("Eligible")
```

### Question 7: Local scope

What happens when you execute this program?

```python
def display():
    message = "Hello"
    print(message)

display()
print(message)
```

### Question 8: Global scope

What is the output?

```python
number = 10

def display():
    print(number)

display()
```

### Question 9: Global keyword

Write a function that increases a global counter by 1.

### Question 10: Automotive application

Write a program that checks:

- If speed is above 80 km/h, print "Overspeed"
- If speed is between 40 and 80 km/h, print "Normal speed"
- If speed is below 40 km/h, print "Low speed"

---

# Day 3 Summary

Today you learned how Python makes decisions.

The most important concept is:

**A condition evaluates to True or False, and Python uses that result to decide which code block should execute.**

Conditional statements are used in almost every real-world application, including:

- Automotive ECU testing
- Sensor monitoring
- Test automation
- Safety warnings
- User input validation
- Embedded software logic

Day 3 is complete when you can write simple `if`, `if-else`, and `if-elif-else` programs without referring to the notes.