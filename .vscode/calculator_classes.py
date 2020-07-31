import math

class Cal:
    def __init__(self):
      pass

    def add(self, num1, num2):
        return num1 + num2

    def minus(self, num1, num2):
        return num1 - num1

    def divide(self, num1, num2):
        return num1/num2

    def multiply(self, num1, num2):
        return num1 * num1

    def power(self, num1, num2):
        return num1 ** num1

    def _sin(self, num1):
        return math.sin(num1)
    
    def _tan(self, num1):
        return math.tan(num1)
        
    def _cos(self, num1):
        return math.cos(num1)

calculate1 = Cal()

num1 = int(input("pleasae enter your first number: "))

print('select your option')
print('+')
print('-')
print('*')
print('/')
print('^')
print('cos')
print('sine')
print('tan')


choice = input('your choice is: ')


if choice == '+':
    num2 = int(input("please enter your second number: "))
    print(f'{num1} + {num2} = {calculate1.add(num1, num2)}')
elif choice == '-':
    num2 = int(input("please enter your second number: "))
    print(f'{num1} - {num2} = {calculate1.minus(num1, num2)}')
elif choice == '*':
    num2 = int(input("please enter your second number: "))
    print(f'{num1} * {num2} = calculate1.{multiply(num1, num2)}')
elif choice == '/':
    num2 = int(input("please enter your second number: "))
    print(f'{num1} / {num2} = {calculate1.divide(num1, num2)}')
elif choice == '^':
    num2 = int(input("please enter your second number: "))
    print(f'{num1} ^ {num2} = {calculate1.power(num1, num2)}')
elif choice == 'cos':
    print(f' cos {num1} = {calculate1._cos(num1)}')
elif choice == 'sine':
    print(f'sin {num1} = {calculate1._sin(num1)}')
elif choice == 'tan':
    print(f'tan {num1} = {calculate1._tan(num1)}')
else:
    print(f'please enter a valid opration')