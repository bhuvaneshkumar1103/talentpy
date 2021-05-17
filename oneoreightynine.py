'''
Mr.Talentpy would like to create a func,on one_or_eight which takes an integer input (no) and
performs following opera,on.
1. Square the number if it is single digit. (Eg: 3, then 3 * 3 = 9)
2. If it is not single digit, square each digits and add. (Eg: 12, then (1*1) + (2*2) = 1+4 = 5
You have to repeat step (1) and (2) un,l you reach 1 or 89. Note that, always your result will reach
1 or 89 for sure. Input must be a posi,ve number.
If the opera,on reaches at the end, 89 return True, if opera,on reaches 1 at the end return False.
Sample Input/Output: 1
• Input: 3
• Output : 3 *3 = 9 => 9 * 9 => 81 => (64+1) = 65 => (36+25) = 61 => (36+1) => 37 = (9+49) => 58
=> (25+64) => 89.
• Explana,on : True
Sample Input/Output: 2
• Input: 10
• Output : 1 square + 0 square = 1+0 = 1
• Explana,on : False
'''
#Create a function name one_or_eight which get a input as a number.
def one_or_eight(no):
    if no>0:
        if no == 1:
            return False
        elif no == 89:
            return True
        else:
# square the single digit number
            if no<10:
                no = no*no
                return one_or_eight(no)
# square the each digit.
            else:
                square = 0
                while(no!=0):
                    n=no%10
                    square = square+n*n
                    no = no//10
                no = square
                return one_or_eight(no)
no = int(input("Enter a Number: "))
result = one_or_eight(no)
print(result)
