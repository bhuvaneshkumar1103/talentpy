'''
Mr.Jochen working on creating application for his school. Here are the following
functions that he would to like create -
1. get_student_marks - which takes student mark1, mark2 and mark3
and return its total.
2. get_student_grade - which calls get_student_marks and returns “A”
grade if mark1 is greater than 50, else it should return grade “B”.
3. validate_marks - which validates mark1, mark2, mark3. Here are the
validations -
1. If any of the mark is less than zero or not a number, this function
should return False.
2. If any of the mark is greater than 25, then this function should
return False.
3. Else, this function should return True
4. validate_student_name - this function should check whether student
name is of length > 5 and less than 25. If name valid, return True, else return False
5. main - Function which should take name and marks (m1, m2, m3
respectively).
a. Call validate_student_name function if it gives False, print “Invalid
Student Name”.
b. If not, Call validate_marks function and if it gives False, print
“Invalid Mark input”.
c. If not, do a simple check, ensure minimum score of each marks
(m1, m2, m3) is greater than or equal to 7. If not, print “You got failed, grades
cannot be calculated”.
d. If not, call get_student_grade method and print the grade which this
function returned as the output.
'''
# Creat a funtion naming get_student_marks which will get mark1,mark2,mark3.
def get_student_marks(mark1,mark2,mark3):
# Sum of mark1,mark2 and mark3.
    total=mark1+mark2+mark3
    return total

# Create a function naming get_student_grade which will get the function get_student_marks as a input.
def get_student_grade(mark1,mark2,mark3):
    if get_student_marks(mark1,mark2,mark3)>50:
        return 'A'
    else:
        return 'B'

# create a function naming validate_marks which validates mark1, mark2, mark3.
def validate_marks(mark1,mark2,mark3):
    
#Check whether the marks are a number or not
    if not(str(mark1).isdigit() and  str(mark2).isdigit() and str(mark3).isdigit()):
        return False
    
    elif mark1<0 or mark2<0 or mark3<0 :
        return False
    elif mark1>25 or mark2>25 or mark3>25:
        return False
    else:
        return True
#create a function naming  validate_student_name, this function should check whether student name.
def validate_student_name(name):
    if len(name)>5 and len(name)<25:
        return True
    else:
        return False
#create a function naming that takes name and marks>
def main(name,m1,m2,m3):
    if validate_student_name(name) == False:
        print("Invalid Student Name")
    elif validate_marks(mark1,mark2,mark3) == False:
        prii=nt("Invalid Mark Input")
    elif not (m1>=7 and m2>=7 and m3>=7):
        print("You got failed, grades cannot be calculated")
    else:
        result = get_student_grade(mark1,mark2,mark3)
        print("The grade is ",result)
        

name = str(input("Enter Your Name:"))
mark1= eval(input("Enter the Mark 1 :"))
mark2= eval(input("Enter the Mark 2 :"))
mark3= eval(input("Enter the Mark 3 :"))

#callin function main.
main(name,mark1,mark2,mark3)
    
