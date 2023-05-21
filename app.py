# print("Hello world, my age is", 100)
# print("how are you")
#variables
# age = 100
# print("He is 11 years")
# print(f"He is {age} years")
#strings
# print("Hello \nhow are you")
# name = 'Tim'
# print(name.lower().islower())
# print((name.index('m')))
# print(name.replace('m','T'))
#numbers
# from math import *
# number = 79
# number2 =str(number)
# print(number2)
# print(f"number is {number}")
# print(abs(-5))
# print(min(1,2,16,30))
# print(sqrt(100))
#getting user input
# name = input("Enter name:")
# age = int(input("Enter age:"))
# print(f"your name is {name} and you are {age} years old")
# sentence = input('Enter the sentence')
#
# word1 = input("enter word to replace:")
# word2 = input("enter word2 to replace:")
# print(sentence.replace (word1,  word2))
# countries =['Uganda', 'uk','ghana','nigeria','york',3]
# countries[0]= 'un'
# print(countries)
# print(type(countries[5]))
#or
# countries =list(('uk',34,'kenya','tz'))
# print(countries)
#list methods
# list1 = [4,3,5,1,6,2,0,9,8]
# list2 =['banana','apples','mangoes','oranges','mangoes']
# # list2.insert(1,'cherry')
# # list2.remove('apples')
# # list2.reverse()
# # list3 =list2.copy()
# # list2.pop(0)
# del list2
# print(list2)
# three = (1,2,'home',3,1)
# string = ('home','land','earth')
# print(type(three[0]))
# def greetings_function(name, age):
#     name =input('Please enter your name')
#     age = input('Enter your age')
#     print('Welcome', name,'.you are',age,'years old')
#
# greetings_function(name='', age='')
# a = False
# b= 5
# if a==b:
#     print('A equals B')
# elif a == False:
#     print('A is false')
# elif a == 'Hey':
#     print('awwsh')
# else:
#     print('A not equals B')
# value = input('Input a value:')
# if type(value) ==str:
#     print(value,'is a string')
# # elif type(value) ==int:
# #     print(value,'is an integer')
# # elif type(value) == list:
# #     print(value,'is string')
# else:
#     print(value,'is not a string')
# my_dict = {
#     'name':'tim',
#     'name2':'tim',
#     'nationality':'African',
#     'Qualification':'College'
# }
# print(my_dict)
# i=1
# while i<6:
#     print(i)
#     i+=1
# mylist = ['ji','ju','jo']
# for item in mylist:
#
#     if item =='ju':
#         break
#     print(item)
# for x in range(3,7):
#     print(x)
# else:
#     print('finished looping')

# my_list = [
#     [1,2,3],
#     [4,5,6],
#     [77,8,9]
# ]
#
# for lists in my_list:
#     for row in lists:
#         print(row)
#basic calculator
'''
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

'''
# try:
#     x = int(input('Input an integer'))
#     print(x)
# except:
#     print('Something went wrong,plz try again')
# else:
#     print('nothing went wrong')
# coun_file= open('countries.txt','r',)
# for lines in coun_file.readlines():
#     print(lines)
#
# coun_file.close()
# coun_file= open('countries.txt','a',)
# coun_file.write('\nThis is a new Country')

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age =age
#
# name = input('Enter your name')
# age = input('Enter your age')
# p1 = Person(name,age)
# print(f'Hello{name},you are {age} years old')
# from new import Student
# class Person(Student):
#     pass
# p1 = Person()
# print(p1.name)
# def hello(name):
#     print(f'hello {name}')
# hello('dijon')

#SigNuP
username1 =input('Enter username:')
password1 =input('Enter password:')
confirmpass = input('Confirm password:')
if password1==confirmpass:
    print('Account created successfulyy')
else:
    print('check your password and try again')
print('Login Now')
username2 = input('Enter username:')
password = input('Enter password:')
if username2 == username1 and confirmpass ==password:
    print(f'Hello {username1} you have logged in successfully')
else:
    print('Invalid credentials')
