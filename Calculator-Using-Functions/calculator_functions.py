import math

print("""
 
▄█████░▄████▄░██░░░░░▄█████░██░░░██░██░░░░░▄████▄░████████░▄█████▄░█████▄
██░░░░░██░░██░██░░░░░██░░░░░██░░░██░██░░░░░██░░██░░░░██░░░░██░░░██░██░░██
██░░░░░██░░██░██░░░░░██░░░░░██░░░██░██░░░░░██░░██░░░░██░░░░██░░░██░█████▀
██░░░░░██████░██░░░░░██░░░░░██░░░██░██░░░░░██████░░░░██░░░░██░░░██░██░░██
▀█████░██░░██░██████░▀█████░▀█████▀░██████░██░░██░░░░██░░░░▀█████▀░██░░██
""") 
# We print the operations options.
print(""" 
1.Sum
2.Minus
3.Multiplication
4.Division
5.Root
6.Power
7.Fractions
""")

# We request parameters.
op = int(input("Choose the operation: ")) 
num1 = int(input("Choose the first number: "))
num2 = int(input("Choose the second number: "))

# We define all the functions.
def sum1(num1, num2):
    return num1 + num2
def minus(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2
def root (num1, num2):
    return math.pow(num1, 1 / num2)
def power (num1, num2):
    return num1 ** num2
def fractions (num1, num2):
    return num1 / num2

# All the conditionals to invoke the functions.
if op == 1:
    result = sum1(num1, num2)
if op == 2:
    result = minus(num1, num2)
if op == 3:
    result = multiplication(num1, num2)
if op == 4:
    result = division(num1, num2)
if op == 5:
    result = root(num1, num2)
if op == 6:
    result = power(num1, num2)
if op == 7:
    result = fractions(num1, num2)
    

print("This is the result:", result)

