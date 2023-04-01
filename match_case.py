a = int(input("enter a first number : "))
b = int(input("enter a second number: "))
op = (input("enter a operator: "))
match op:
    case '+':
        print("the sum of two numbers is = ", a+b)
    case '-':
        print("the subtraction of two numbers is = ", a - b)
    case '*':
        print("the multiplication of two numbers is = ", a * b)
    case '/':
        print("the division of two numbers is = ", a / b)

