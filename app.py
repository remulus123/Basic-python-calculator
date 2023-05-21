
#basic calculator

num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))
op = input('Enter the operator')
if op == '+':
    print('Sum is ', num1+num2)
elif op =='-':
    print('Difference is ', num1-num2)
elif op =='*':
    print('Multiplication is', num1*num2)
elif op == '/':
    print('Division is', num1/num2)
else:
    print('Invalid operator')


