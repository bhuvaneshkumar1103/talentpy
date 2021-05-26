'''
Write a list comprehension to find factorial of each numbers in a given list L if and only
if the numbers are even. For Example: If L = [1,2,3,4] then output should be [2, 24].
'''
import math
lt = [1,2,3,4,5,6,7,8,9,10]
# the list comprehension will save the factorial of each even digit in the new list
fact_lt = [math.factorial(x) for x in lt if x%2 ==0]
print(fact_lt)