'''
Create a lambda function which takes two inputs X and Y and performs X power Y
operation and returns the output. For Example: If X is 2 and Y is 3, then 2 power 3 = 2
* 2 * 2 = 8.
'''
# syntax for the lambda function is = lambda inputs:expression
lam_fun= lambda x,y: x**y
x = eval(input("Enter a number: "))
y = eval(input("Enter a number: "))
print(lam_fun(x,y))