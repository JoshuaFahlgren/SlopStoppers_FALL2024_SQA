'''
Team Name: Slop Stoppers

Team Members:
- Joshua Fahlgren
- Mathew Rogers

'''

import random
import math

def add(v1, v2):
    if v1.isnumeric() and v2.isnumeric():
        v1 = float(v1)
        v2 = float(v2)
        return v1 + v2
    else:
        return "One of the inputs is invalid."

def subtract(v1, v2):
    if v1.isnumeric() and v2.isnumeric():
        v1 = float(v1)
        v2 = float(v2)
        return v1 - v2
    else:
        return "One of the inputs is invalid."

def multiply(v1, v2):
    if v1.isnumeric() and v2.isnumeric():
        v1 = float(v1)
        v2 = float(v2)
        return v1 * v2
    else:
        return "One of the inputs is invalid."

def divide(v1, v2):
    if v1.isnumeric() and v2.isnumeric():
        v1 = float(v1)
        v2 = float(v2)
        if v2 != 0:
            return v1 / v2
        else:
            return "Division by zero error."
    else:
        return "One of the inputs is invalid."

def power(v1, v2):
    if v1.isnumeric() and v2.isnumeric():
        v1 = float(v1)
        v2 = float(v2)
        try:
            return math.pow(v1, v2)
        except OverflowError:
            return "Result too large to compute."
    else:
        return "One of the inputs is invalid."

def fuzzValues(val1, val2, operation):
    if operation == 'add':
        return add(val1, val2)
    elif operation == 'subtract':
        return subtract(val1, val2)
    elif operation == 'multiply':
        return multiply(val1, val2)
    elif operation == 'divide':
        return divide(val1, val2)
    elif operation == 'power':
        return power(val1, val2)
    else:
        return "Invalid operation"

def simpleFuzzer():
    # Test cases for addition
    print("Testing Addition:")
    print(fuzzValues('10', '5', 'add'))
    print(fuzzValues('abc', '5', 'add'))
    print(fuzzValues('0', '0', 'add'))

    # Test cases for subtraction
    print("\nTesting Subtraction:")
    print(fuzzValues('10', '5', 'subtract'))
    print(fuzzValues('5', '10', 'subtract'))
    print(fuzzValues('abc', '5', 'subtract'))

    # Test cases for multiplication
    print("\nTesting Multiplication:")
    print(fuzzValues('10', '5', 'multiply'))
    print(fuzzValues('0', '5', 'multiply'))
    print(fuzzValues('abc', '5', 'multiply'))

    # Test cases for division
    print("\nTesting Division:")
    print(fuzzValues('10', '5', 'divide'))
    print(fuzzValues('10', '0', 'divide'))
    print(fuzzValues('abc', '5', 'divide'))

    # Test cases for power
    print("\nTesting Power:")
    print(fuzzValues('2', '3', 'power'))
    print(fuzzValues('2', '1000', 'power'))
    print(fuzzValues('abc', '5', 'power'))

def randomFuzzer(num_tests=10):
    operations = ['add', 'subtract', 'multiply', 'divide', 'power']
    
    for _ in range(num_tests):
        # Generate random numbers as strings
        v1 = str(random.randint(-100, 100))
        v2 = str(random.randint(-100, 100))
        op = random.choice(operations)
        
        result = fuzzValues(v1, v2, op)
        print(f"Operation: {op}, Values: {v1}, {v2}, Result: {result}")

if __name__=='__main__':
    print("Running Simple Fuzzer Tests:")
    simpleFuzzer()
    print("\nRunning Random Fuzzer Tests:")
    randomFuzzer()