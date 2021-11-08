from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


def calculator():
  print(logo)
  num1 = float(input("What is the first number? "))

  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
  }

  for x in operations:
    print(x)

  should_continue = True
  while should_continue:
    operation_symbol = input("Choose one symbol from above. ")
    num2 = float(input("What is the second number? "))
    if operation_symbol == "+":
      answer = num1 + num2
    elif operation_symbol == "-":
      answer = num1 - num2
    elif operation_symbol == "*" or  operation_symbol == "x":
      answer = num1 * num2
    elif operation_symbol == "/":
      answer = num1 / num2

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"If you want to continue with {answer} press 'y', if you want to exit press 'n' ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()