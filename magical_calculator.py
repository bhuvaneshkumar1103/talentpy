'''
You are going to design a magical calculator with the following functions.
• Function that takes input and calculates it’s factorial. (A)
• Function that takes input and calculate it’s sum of digits. (B)
• Function that takes input and find’s the largest digit in the input. (C)
- Implement all the above functions.
- Get input and pass the input to factorial function (A), get the output from
factorial function and pass it as input to sum of digits function (B). Get the output
from sum of digits function, add the output with random 5 digit number and pass
the outcome to largest digit function (C) and print the output that you receive from
function C.
Sample I/O:
• Input 5
• Output of A = 120
• Output of B(120) = 1+2+0 = 3
• Output of C(3 + 10000 = 10003) = 3 (Here 10000 is the random number)
• Hence output is 3 , where 3 is the largest digit of 10003.
'''
import random
# create a funtion name factorial which gets a input name a to find the factorial of the input
def factorial(a):
    fact=1
    while(a>1):
        fact=fact*a
        a=a-1
    return fact
''' create a function name sumOfDigit which gets the input from the function factorial
    and finds the sum of digit. '''
def sumOfDigits(c):
    sum = 0
    n = factorial(a)
    while(n!=0):
        sum =  sum + n%10
        n = n//10
    return sum
''' create a function name largestDigits which gets the input from the function sumofdigit
    and the input with a 5 digit random number which is 10000 and finds the largest digit
    among the five digit number.'''
def largestDigits(d):
    output = str(d)
    largestdigit = output[0]
    for i in range(0,len(output),1):
                  if largestdigit<output[i] :
                      largestdigit = output[i]
    return largestdigit
a = eval(input("Enter a Number:"))
''' calling the functions with one another.'''
result = largestDigits(sumOfDigits(factorial(a))+random.randint(10000, 99999))
print(result)
