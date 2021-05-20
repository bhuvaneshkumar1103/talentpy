'''
Create a func,on difference which takes a string S and character K. Find the difference between
first occurrence of K and last occurrence of K in string S. Convert the input to lower case before
processing.
Check for following condi,ons :
1. If K not occurred in S, return “K not found in S”.
2. If K occurred only once in S, return “Difference can’t be calculated”.
3. If K occurs more than once, return count of difference.
Sample I/O:
• Input: S= ‘talentpy', K=‘a’ => output: “Difference can’t be calculated”,
• Input: S=“science”, K=‘c’ => output: 3.
'''
def difference(s,k):
    s = s.lower()
    k = k.lower()
# get the first occurence of the character in the given string.
    firstindex = s.find(k)
# get the last occurence of the character in the given string.
    lastindex = s.rfind(k)
# checking the difference between the first and the last occurence and return the respective answer.
    if firstindex == -1 :
        return "K not found in the given string."
    elif lastindex == -1 or lastindex == firstindex :
        return "Difference can’t be calculated."
    else:
        diff = lastindex-firstindex
        return diff-1
s = str(input("Enter a string: "))
k = str(input("ENter the character to be searched in the given string: "))
result = difference(s,k)
print(result)
