
from classes.week00.second_class.utils import clear_screen
'''
#13 - Conditional Logic
Ask the user for a number and print whether it is positive, negative, or zero.
'''
num = float(input("Enter number here: ))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("Number is negative.")
else:
    print("Number is zero.add(element)")

#CORRECT ANSWER
txt = "Please enter a number: "
while True:
    try:
        num = int(input(txt))
        i = 1
        while 1 < 6:
            print(i)
            if i ==3:
                break
                i +=1
    except ValueError:
        txt = "a number: "

#if looking for a number, put in WHILE loop, but don't need if you are looking for text
                  



pause=input('pause')
clear_screen()

'''
#14 - Even/Odd Check
Ask the user for a number and print if it is even or odd.
'''
num = int(input("Enter number here: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number.")

#Correct Answer

if num % 2 == 0: print("even")



pause=input('pause')
clear_screen()

'''
#15 - Boolean Operators
Ask the user for two numbers and check if both are positive, either is positive, or none is positive.
'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > 0 and num2 > 0:
    print("Both are positive")
elif num1 > 0 or num2 > 0:
    print("At least one value is positive")
else:
    print("Both are negative")



pause=input('pause')
clear_screen()

'''
#16 - For Loop
Print all numbers from 1 to 20, skipping multiples of 3.
'''
for idx in range(1,21):
    if i % 3 == 0:
    print(i)

#QUESTION HERE!!!
for idx in range (1,21):
    if i % 3 != 0:
    print(idx)

pause=input('pause')
clear_screen()

'''
#17 - While Loop
Ask the user to guess a secret number (hardcoded) until they get it right.
'''
Secret_num = 6

while True:
    guess = int(input("Guess what the number is: "))
if guess == Secret_num:
    print("Correct!")

else:
    print("Wrong")

#Correct
secret = 6
num = int(input("enter a number"))

while True:
    try

pause=input('pause')
clear_screen()

'''
#18 - Break / Continue
Print numbers 1-10 but stop printing when you reach 7 and skip 3.
'''
for i in range(1,11):
    if i == 3:
        continue
    if i == 7:
        break



pause=input('pause')
clear_screen()

'''
#19 - Function Definition
Write a function square(x) that returns the square of a number and test it.
'''
# enter code here



pause=input('pause')
clear_screen()

'''
#20 - Function with Mutable Argument
Write a function add_item(lst, item) that appends item to lst and observe the effect on the original list.
'''
def add_item(1st, item):
    1st.append(item)

#complete code

pause=input('pause')
clear_screen()

'''
#21 - Comments / Documentation
Write a function greet(name) with single-line and multi-line comments explaining each step.
'''
def greet(name):
"""
greet(name) Takes the argument "name" and prints greeting.



pause=input('pause')
clear_screen()

'''
#22 - Combining Tools
Ask the user to enter 5 names. Store them in a list, capitalize each name, sort the list, and print it.
'''
# enter code here



pause=input('pause')
clear_screen()

