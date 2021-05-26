#import thr decrator function from the package.
from caller_decorator import perform_n_calls
def console():
    print("TalentpY")
N= eval(input("Enter how many times to print the string: "))
#calling the decrator funtion to add aditional behaviour to this console function.
console = perform_n_calls(console,N)
