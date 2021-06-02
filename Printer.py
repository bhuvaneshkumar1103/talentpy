#create a class Printer which has constructor and a method print_me(data)
class Printer:
    def __init__(self):
        pass
    # this function will return the data whatever it is passed as a argument.
    def print_me(self,value):
        return value

obj  = Printer()
result = obj.print_me("Welcome")
print(result)

'''
Output:

        Welcome  -> The printer class will return the argument as ouput, 
        which is passed has a parameter to the function.
'''