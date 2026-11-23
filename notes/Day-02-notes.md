# 100 Days of Code – Python
## Day 2: Data Types, Numbers and Mathematical Operations

**Topics Covered:**

1. Data Types
2. Numbers in Python
3. Mathematical Operations
4. Operator Precedence
5. Type Conversion
6. Working with Numbers
7. Common Errors

---

# 1. What Are Data Types?

A data type tells Python what kind of value a variable contains.

For example:

```python
name = "Ashina"
age = 27
height = 167.5
is_learning = True
```

Here, each variable stores a different type of information.

| Variable | Value | Data Type |
|---|---|---|
| name | "Ashina" | String |
| age | 27 | Integer |
| height | 167.5 | Float |
| is_learning | True | Boolean |

Python automatically identifies the data type when we assign a value.

## Why do we need data types?

Imagine that we are developing an automotive application.

We need to store:

- Vehicle name
- Vehicle speed
- Engine temperature
- Whether the engine is running

Each value has a different purpose and type.

```python
vehicle_name = "Car"
vehicle_speed = 80
engine_temperature = 95.5
engine_running = True
```

Data types help Python understand how values should be handled.

---

# 2. Basic Data Types in Python

Python has several built-in data types.

The most common beginner data types are:

1. String (`str`)
2. Integer (`int`)
3. Float (`float`)
4. Boolean (`bool`)

## 2.1 String – str

A string is a sequence of characters.

It is used to store text.

Examples:

```python
name = "Ashina"
city = "Bengaluru"
message = "Learning Python"
```

Strings are written inside single or double quotation marks.

```python
print(type(name))
```

Output:

```text
<class 'str'>
```

The `type()` function tells us the data type of a value.

## 2.2 Integer – int

An integer is a whole number without a decimal point.

Examples:

```python
age = 27
vehicle_speed = 80
temperature = -10
```

Integers can be:

- Positive
- Negative
- Zero

Example:

```python
number = 100

print(type(number))
```

Output:

```text
<class 'int'>
```

## 2.3 Float – float

A float is a number that contains a decimal point.

Examples:

```python
height = 167.5
temperature = 36.8
voltage = 12.5
```

Example:

```python
voltage = 12.5

print(type(voltage))
```

Output:

```text
<class 'float'>
```

Floats are useful for measurements such as:

- Voltage
- Temperature
- Speed
- Current
- Sensor values

## 2.4 Boolean – bool

A Boolean represents one of two values:

- `True`
- `False`

Example:

```python
engine_running = True
door_open = False
```

Boolean values are used for conditions and decision-making.

Example:

```python
engine_running = True

print(type(engine_running))
```

Output:

```text
<class 'bool'>
```

Important: Python uses capital letters for Boolean values.

Correct:

```python
True
False
```

Incorrect:

```python
true
false
```

---

# 3. Numbers in Python

Python supports different numeric types.

The most common are:

- `int`
- `float`
- `complex`

## 3.1 Integer numbers

```python
a = 10
b = 20
c = -5
```

Integers do not have a decimal point.

## 3.2 Floating-point numbers

```python
a = 10.5
b = 3.14
c = -2.75
```

Floats contain a decimal point.

## 3.3 Complex numbers

Complex numbers contain a real part and an imaginary part.

Example:

```python
number = 3 + 4j

print(number)
print(type(number))
```

Output:

```text
(3+4j)
<class 'complex'>
```

The letter `j` represents the imaginary part in Python.

Complex numbers are used in advanced mathematical and electrical engineering calculations.

For example, AC circuit analysis often uses complex numbers to represent impedance.

---

# 4. Mathematical Operations in Python

Python can perform mathematical calculations using operators.

| Operator | Operation | Example | Result |
|---|---|---|---|
| `+` | Addition | 10 + 5 | 15 |
| `-` | Subtraction | 10 - 5 | 5 |
| `*` | Multiplication | 10 * 5 | 50 |
| `/` | Division | 10 / 5 | 2.0 |
| `//` | Floor division | 10 // 3 | 3 |
| `%` | Modulus | 10 % 3 | 1 |
| `**` | Exponentiation | 2 ** 3 | 8 |

## 4.1 Addition

The `+` operator adds two numbers.

```python
a = 10
b = 20

result = a + b

print(result)
```

Output:

```text
30
```

## 4.2 Subtraction

The `-` operator subtracts one number from another.

```python
a = 20
b = 5

result = a - b

print(result)
```

Output:

```text
15
```

## 4.3 Multiplication

The `*` operator multiplies two numbers.

```python
a = 10
b = 5

result = a * b

print(result)
```

Output:

```text
50
```

## 4.4 Division

The `/` operator performs division.

```python
a = 10
b = 2

result = a / b

print(result)
```

Output:

```text
5.0
```

Important: The `/` operator returns a float, even when the result is a whole number.

Example:

```python
print(10 / 2)
```

Output:

```text
5.0
```

## 4.5 Floor Division

The `//` operator performs floor division.

It returns the quotient rounded down to the nearest integer value.

```python
print(10 // 3)
```

Output:

```text
3
```

Explanation:

10 divided by 3 gives approximately 3.333.

Floor division returns 3.

Important: Floor division does not always mean simply removing the decimal part. It rounds toward negative infinity.

Example:

```python
print(-10 // 3)
```

Output:

```text
-4
```

## 4.6 Modulus

The `%` operator returns the remainder after division.

```python
print(10 % 3)
```

Output:

```text
1
```

Explanation:

10 divided by 3:

- Quotient = 3
- Remainder = 1

Therefore:

```python
10 % 3
```

returns:

```text
1
```

### Real-world example: Checking even or odd numbers

```python
number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

Output:

```text
Even number
```

We will study `if` and `else` in a later lesson.

## 4.7 Exponentiation

The `**` operator raises a number to a power.

```python
print(2 ** 3)
```

Output:

```text
8
```

Explanation:

2 × 2 × 2 = 8

Another example:

```python
print(5 ** 2)
```

Output:

```text
25
```

---

# 5. Operator Precedence

Operator precedence determines which mathematical operation Python performs first.

Python follows a specific order.

For example:

```python
result = 2 + 3 * 4

print(result)
```

Output:

```text
14
```

Why?

Multiplication has higher precedence than addition.

First:

3 × 4 = 12

Then:

2 + 12 = 14

## Common operator precedence order

| Priority | Operator |
|---|---|
| Highest | `()` |
| | `**` |
| | `*`, `/`, `//`, `%` |
| Lowest among these | `+`, `-` |

## Example with parentheses

```python
result = (2 + 3) * 4

print(result)
```

Output:

```text
20
```

Parentheses are evaluated first.

2 + 3 = 5

5 × 4 = 20

Important: Use parentheses when you want to make the calculation order clear.

---

# 6. Type Conversion

Type conversion means changing a value from one data type to another.

Python provides built-in functions for type conversion.

Common functions:

- `int()`
- `float()`
- `str()`
- `bool()`

## 6.1 Convert to Integer – int()

The `int()` function converts a compatible value into an integer.

Example:

```python
number = int(10.8)

print(number)
```

Output:

```text
10
```

Important: `int()` truncates the decimal part. It does not round to the nearest integer.

Example:

```python
print(int(9.9))
```

Output:

```text
9
```

## 6.2 Convert to Float – float()

The `float()` function converts a compatible value into a floating-point number.

```python
number = float(10)

print(number)
```

Output:

```text
10.0
```

We can also convert a numeric string.

```python
number = float("12.5")

print(number)
```

Output:

```text
12.5
```

## 6.3 Convert to String – str()

The `str()` function converts a value into a string.

```python
age = 27

age_text = str(age)

print(age_text)
print(type(age_text))
```

Output:

```text
27
<class 'str'>
```

The value is now text, not an integer.

## 6.4 Convert to Boolean – bool()

The `bool()` function converts a value into a Boolean.

```python
print(bool(1))
print(bool(0))
```

Output:

```text
True
False
```

Some common Boolean conversions:

| Value | Result |
|---|---|
| `bool(1)` | True |
| `bool(0)` | False |
| `bool("")` | False |
| `bool("Hello")` | True |
| `bool([])` | False |

Important: A non-empty string is considered `True`, even if it contains the text `"False"`.

```python
print(bool("False"))
```

Output:

```text
True
```

Because `"False"` is a non-empty string.

---

# 7. Type Conversion and User Input

The `input()` function receives information from the user.

Important: The `input()` function always returns a string.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

```text
27
```

Output:

```text
<class 'str'>
```

Even though the user entered a number, Python stores it as a string.

## Example: Adding two numbers entered by the user

Incorrect approach:

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
```

If the user enters:

```text
10
20
```

Output:

```text
1020
```

Why?

Because both values are strings.

The `+` operator joins strings instead of adding numbers.

## Correct approach

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a + b

print(result)
```

If the user enters:

```text
10
20
```

Output:

```text
30
```

Explanation:

1. `input()` receives the value as a string.
2. `int()` converts it into an integer.
3. Python performs addition.
4. `print()` displays the result.

---

# 8. Mathematical Operations with Variables

We can use variables to perform calculations.

Example:

```python
length = 10
width = 5

area = length * width

print("Area:", area)
```

Output:

```text
Area: 50
```

## Example: Vehicle speed calculation

Suppose a vehicle travels 120 km in 2 hours.

Formula:

Speed = Distance / Time

```python
distance = 120
time = 2

speed = distance / time

print("Vehicle speed:", speed, "km/h")
```

Output:

```text
Vehicle speed: 60.0 km/h
```

This is a simple example of using Python for automotive calculations.

---

# 9. Common Mistakes

## Mistake 1: Adding a string and an integer

Incorrect:

```python
age = "27"

print(age + 5)
```

This produces a `TypeError`.

Correct:

```python
age = int("27")

print(age + 5)
```

Output:

```text
32
```

## Mistake 2: Dividing by zero

```python
print(10 / 0)
```

This produces:

```text
ZeroDivisionError
```

Division by zero is not allowed.

## Mistake 3: Confusing `/` and `//`

```python
print(10 / 3)
print(10 // 3)
```

Output:

```text
3.3333333333333335
3
```

`/` performs normal division.

`//` performs floor division.

## Mistake 4: Confusing string and number

```python
number = "100"
```

This is a string, not an integer.

To convert it:

```python
number = int("100")
```

---

# 10. Complete Day 2 Example Program

This program combines data types, variables, type conversion, and mathematical operations.

```python
# Day 2 - Python Data Types and Operations

# Store vehicle information
vehicle_name = "Smart Vehicle"
distance = 150
time = 3

# Display data types
print(type(vehicle_name))
print(type(distance))
print(type(time))

# Calculate average speed
speed = distance / time

print("Vehicle Name:", vehicle_name)
print("Distance:", distance, "km")
print("Time:", time, "hours")
print("Average Speed:", speed, "km/h")

# Demonstrate mathematical operations
print("Addition:", distance + time)
print("Subtraction:", distance - time)
print("Multiplication:", distance * time)
print("Division:", distance / time)
print("Floor Division:", distance // time)
print("Remainder:", distance % time)
print("Power:", distance ** 2)
```

---

# 11. Day 2 Quick Revision

| Concept | Meaning |
|---|---|
| `str` | Text |
| `int` | Whole number |
| `float` | Decimal number |
| `bool` | True or False |
| `type()` | Checks data type |
| `int()` | Converts to integer |
| `float()` | Converts to float |
| `str()` | Converts to string |
| `bool()` | Converts to Boolean |
| `/` | Division |
| `//` | Floor division |
| `%` | Remainder |
| `**` | Power |
| `input()` | Receives user input as a string |

---

# 12. Day 2 Practice Questions

Try solving these yourself.

### Question 1
Create variables for your age, height, and name. Print their data types.

### Question 2
What is the output?

```python
print(10 + 5 * 2)
```

### Question 3
What is the difference between `/` and `//`?

### Question 4
Find the output:

```python
print(17 % 5)
```

### Question 5
Convert the string `"100"` into an integer and add 50.

### Question 6
Why does this program print `1020` instead of `30`?

```python
a = input("Enter a number: ")
b = input("Enter another number: ")

print(a + b)
```

### Question 7
Calculate the average speed of a vehicle that travels 200 km in 4 hours.

### Question 8
What is the output?

```python
print(2 ** 4)
```

### Question 9
Identify the data type:

```python
temperature = 36.5
```

### Question 10
Write a Python program that receives two numbers from the user and displays their sum, difference, multiplication, and division.

---

**Day 2 Status: In Progress / Completed after practice**

Today's concepts are the foundation for future Python programs, especially sensor-data processing, automotive calculations, and test automation.