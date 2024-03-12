#Calculator

# add
def add(a, b):
  return a + b

# subtract
def subtract(a, b):
  return a - b

# multiply
def multiply(a, b):
  return a * b

# divide
def divide(a, b):
  return a / b

operations = {'+': add, 
              '-': subtract,
              '*': multiply,
              '/': divide}

cont = True

while cont == True:

    num1 = int(input("What's the first number? "))
    operation = input("What's the operation (+, -, *, /)? ")
    num2 = int(input("What's the second number? "))

    operation_function = operations[operation]
    answer = operation_function(num1, num2)

    print(f"{num1} {operation} {num2} = {answer}")
    keep_going = input("Would you like to do another calculation? Please type 'y' or 'n': ")
    if keep_going == 'n':
      cont = False