'''
Create a func,on to sum up all posi,ve argument inputs. Inputs ranges from 0 to N,
where N can be any posi,ve number.
'''
# create a function name sum_all_number which takes a input as a number.
def sum_all_number(no):
    sum = 0
# suming all the numbers upto no.
    if no>0:
        for i in range(0,no+1,1):
            sum = sum + i
    return sum

no = eval(input("Enter a Number: "))
result = sum_all_number(no)
print("The Sum of ",no," Numbers :",result)
