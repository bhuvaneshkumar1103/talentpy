'''
create a class student which as parameterised constructor and also has a function 
with getter and setter using Decrators.
'''
class student:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    # this name_change function is a getter function using @property and returs the argument as output.
    @property
    def name_change(self):
        return self.name
    #this name_change function is a setter function using @function name.Setter and do the following changes in the name.
    @name_change.setter
    def name_change(self,name):
        if self.gender == 'M':
            self.name = "Mr." + name
        else:
           self.name = "Ms." + name
        
name = str(input("Enter the name: "))
gender= str(input("Enter the 1st letter fo gender: "))
stud = student(name,gender)
stud.name_change = name
print(stud.name_change)

'''
Output:
   Enter the name: Bhuvanesh
   Enter the 1st letter fo gender: M
   o/p = Mr.Bhuvanesh
   
   Enter the name: Tamilarasi
   Enter the 1st letter fo gender: F
   o/p = Ms.Tamilarasi
'''