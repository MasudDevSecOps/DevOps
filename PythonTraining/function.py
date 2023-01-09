first_name = 'Masud'
last_name = ' Rahman'

print(first_name + last_name)


# function 1
def greeting():  # head
    print('Hello Mr! Hope you are you doing well')  # body
    print('Today is very cold')  # body
    print('Stay warm!')


greeting()


# function 2
def sahada():
    print('There is no god but Allah')
    print('Muhammad is the messenger of Allah')


sahada()

# Printing function
print(greeting(), sahada())


# 3rd function
def all_function():
    greeting()
    sahada()


all_function()


# Defining a function
def print_star_war_greeting():
    print('May the force be with you')
    print('and also with you')


print_star_war_greeting()


# Parameter and arguments
def greet(name):  # name is parameter here (a variable)
    print('Hello!', name)
    print('How are you?')


greet('John')


def something(x):
    return 5 * x


a = something(1000000000)
print(a)


# Function from class

def students_info():
    students = ['Faysal', 'Mohiuddin', 'Masud', 22]
    print(students)


students_info()


# another one

def add(x=5, y=10):
    return x + y


print(add())


# Write a Python function to sum all the numbers in a list
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum():  # Defining function sum()
    sample_list = [8, 2, 3, 0, 7]  # list
    total = 0  # total will add
    for n in sample_list:
        total = total + n
    print(total)


sum()


def new_sum():
    total = 0
    new_list = [8, 2, 3, 0, 7]
    print(len(new_list))

    for elements in range(2, len(new_list)):
        total = total + new_list[elements]
    print(total)


new_sum()


# function of a string and print the portion of the list

def country():
    nameOfCountry = ['B', 'a', 'n', 'g', 'l', 'a', 'd', 'e', 's', 'h']
    bucket = ' '
    for element in nameOfCountry[0:4]:
        bucket = bucket + element
    print(bucket)


country()


# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def multiply():
    m_list = [8, 2, 3, -1, 7]
    total = 1
    for numbers in m_list:
        total = total * numbers
    print(total)


multiply()


# Write a Python program to reverse a string
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def newReverseFunction():
    sampleString = "1234abcd"[::-1]
    '''
    the slice statement [::-1] means start at the end of the string and end at position 0, 
    move with the step -1, negative one, which means one step backwards.
    '''
    print(sampleString)


newReverseFunction()


def reverse(string):
    string = "".join(reversed(string))
    return string


s = "abcd1234"
print(reverse(s))


# 1. Python function that prints a text

# create a function using def keyword
def hello_function():
    # definition of the function/anything you want this function to do
    print('Welcome to the python world')


# calling the function
hello_function()

#
