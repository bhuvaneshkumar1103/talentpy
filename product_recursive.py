'''
Write python recursive function to perform multiplication of all elements of list L.
'''
#the function multiply will call itself untill lenth of the list.
def multiply(L,n = 0):
    prod = 1
    if n < len(L):
        prod = L[n]*multiply(L,n+1)
    return prod
L = [1,2,3,4,5,6,7,8,9]
print("The product of the list: ",end = "")
print(multiply(L))

