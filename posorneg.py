''' To check whether the given number is positive or negative ot null -
 1. first create  a function name check_number
 2. check if the number is less than 0 return as negative
 3. check if the number is greater than 0 return as positive
 4. check if the number is equal to 0 return as NULL
 5. finallly print the result.'''
def check_number(n):
    if n>0:
        return "Positive"
    elif n<0:
        return "Negative"
    else:
        return "Null"
n = eval(input("Enter a Number:"))
result = check_number(n)
print("The Given Number is ",result)
