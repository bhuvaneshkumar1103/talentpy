'''
Write python script to add elements of list L using reduce() function.
'''
import functools
L = [1,2,3,4,5,6,7,8,9]
print("The sum of elements in the list is : ",end ="")
'''
The reduce function will take two arguments and give the 
result. Now again takes two arguments one is the result of the 
previous one and one from the list. Like this it will executes till no more 
elements in the container.
'''
print(functools.reduce(lambda a,b: a+b,L))