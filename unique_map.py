'''
Write a function called is_unique. This function should take a string and should check
whether all characters of the string is unique/not. Example: If the input string is
“abcd”, all characters are unique, hence it should return True. Another example, if the
string is “abaa”, then this function should return False.
1. Create a List L of size 10 with random strings of length > 1.
2. Write a python snippet to check is_unique nature for all elements of L. (Hint:
Use map function)
3. Apply filter function, to get only unique elements from L.
'''
from typing import Counter
# the function to return the unique elements in the fiven list.
def is_unique(a):
# counting the instance of the string.
    freq = Counter(a)
    return len(freq)==len(a)
L =  ["hi","hello","bhuvi","computer","science","python","java","selenium","dockers","Engineering"]
map_fun = map(is_unique,L)
print(list(map_fun))
fil_fun = filter(is_unique,L)
print(list(fil_fun))
