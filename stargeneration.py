'''
Create a python func,on which takes a number N and generates following star
pacern accordingly. N ranges from 1 to any posi,ve number. Make sure if N is not passed as
argument while calling func,on, it should take 3 as it’s default value.
Example: N = 4
Output:
*
@@
***
@@@@
Example: N = 2
*
@@
'''
def star_pattern(n=3):
    if n>0:
        for i in range(1,n+1,1):
            if (i%2)== 0:
                print('@'*i)
            else:
                print('*'*i)
n = eval(input("Enter a Number: "))
star_pattern(n)
