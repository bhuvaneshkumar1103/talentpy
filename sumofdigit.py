'''
Create a function to compute sum of digits. Call this sum of digits function
to find the sum of digits of numbers ranges from 1001 to 22000.
'''
# Create a funcation name sumOfDigit.
def sumOfDigit(i):
# declare a variable name sum and intially assign 0 to store the sum value of the digits. 
    sum = 0
    while(i!=0):
#Formula for calculating the sum of digits.
        sum = sum+(i%10)
#updating the n value for next loop.
        i=i//10
    return sum
result=0
for i in range(1001,22001,1):
#calling the function and assign its result to the result1 variable.
    result1 = sumOfDigit(i)
    result = result+result1
print("The sum of numbers range from 1001 to 22000 is:",result)
