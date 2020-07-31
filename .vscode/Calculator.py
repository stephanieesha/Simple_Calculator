import math

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
    print(f'{num1} + {num2} = {num1 + num2}')
elif choice == '-':
    num2 = int(input("please enter your second number: "))
    print(f'{num1} - {num2} = {num1 - num2}')
elif choice == '*':
    num2 = int(input("please enter your second number: "))
    print(f'{num1} * {num2} = {num1 * num2}')
elif choice == '/':
    num2 = int(input("please enter your second number: "))
    print(f'{num1} / {num2} = {num1 / num2}')
elif choice == '^':
    num2 = int(input("please enter your second number: "))
    print(f'{num1} ^ {num2} = {num1 ** num2}')
elif choice == 'cos':
    print(f' cos {num1} = {math.cos(num1)}')
elif choice == 'sine':
    print(f'sin {num1} = {math.sin(num1)}')
elif choice == 'tan':
    print(f'tan {num1} = {math.tan(num1)}')
else:
    print(f'please enter a valid opration')
    