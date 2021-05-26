'''
Create three functions as follows -
1. def remove_vowels(string) - which will remove all vowels from the given
string. For example if the string given is “aeiru”, then the return value should
be ‘r’
2. def remove_consonants(string) - which will remove all consonants from
given string. For example, if the string given is “aeri”, then the return value
should be ‘aei’.
3. def caller -> This function should 2 parameters
1. Function to call
2. String argument
This caller function should call the function passed as a parameter, by
passing second parameter as the input for the function. Example: caller(remove_vowles,
“aeiru”) should call remove_vowels function and should return ‘r’ as the output.
'''
def remove_vowels(st) :
    vowel  = ['A','E','I','O','U','a','e','i','o','u']
    for i in st:
        if i in vowel:
# it will replace the vowels in the string
           st =  st.replace(i,'')
    return st
def remove_consonants(st):
    vowel  = ['A','E','I','O','U','a','e','i','o','u']
    for i in st:
        if i not in vowel:
# it will replace all the consonants in the string
            st = st.replace(i,'')
    return st
'''It will call the function which was passed has the 1st parameter and 
give the input for the function which was passed has the 2nd parameter.  
'''
def caller(func,st):
    return func(st)
st = str(input("Enter a string: "))
print("Which Operation should be done in this string !!!")
print("\n 1.remove_vowels \n 2.remove_consonants ")
func = eval(input("Enter the operation name: "))
result = caller(func,st)
print(result)