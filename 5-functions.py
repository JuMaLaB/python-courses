# Program greeting start
def greeting(name):
    print('Hello', name)

name = input('Enter your name:\n')
greeting(name)

another_name = input('Enter another name:\n')
greeting(another_name)

# Program addition start
def addition(a, b):
    return a + b

def main():
    num1 = float(input('Enter number 1:\n'))
    num2 = float(input('Enter number 2:\n'))

    res = addition(num1, num2)
    print('Result of addition is:', res)

main()