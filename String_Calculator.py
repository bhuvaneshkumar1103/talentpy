'''
String Calculator - Implement String calculator with following functions.
• Function that reverses the given string S. (A)
• Function that returns total A’s available (it can be ‘a’ or ‘A’) int given
string S. (B)
• Function that takes 2 inputs string S and index and returns element at
given index. If the index is not available, it should return 0 as the
output. (C)
• Function that multiples given string 5 times (D)
- Implement all the above functions.
- Get input and pass it to the reverse function, get the output from it and call
function C, function C takes 2 params, first param should be output from function
A and second param should be output from function B. Get the output. If the
output is not 0, call function D and print output. Else call print “Completed without
multiply” as the output.
Sample I/O:
Input: “Hari”
Output:
- Reverse of Hari => iraH
- Output from function C => C(“iraH”, 1) => r
- Final output = 5 times of r = rrrrr.
'''
''' Create a function name string_reverse which will take a input as string
    and return the reverse string'''
def string_reverse(s):
    return s[::-1]
''' Create a function name A_available which will take a input as string and
    return the no of 'A' or 'a' in the given string.'''
def A_available(s):
    count = 0
    for i in s:
        if i =='A' or i == 'a':
            count +=1
    return count
''' Create a function name Return_Element which will take two parameters one is output
    of the string_reverse and the another one is output of the A_avaialable function.'''
def Return_Element(c,n):
    if n<len(c):
        return c[n]
    else:
        return 0
''' Create a function name multiple_string which will take input from the output of
    the function Return_Element and the print the output 5times.'''
def multiple_string(d):
        print(d*5)
Input = str(input("Enter a String: "))
#calling the function multiple_string.
multiple_string(Return_Element(string_reverse(Input),A_available(Input)))

    
