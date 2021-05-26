'''
generator which will give the prime numbers from 1 to 5000.
'''
def all_prime():
           
    for num in range(1, 5000):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                 break
            else:
                yield num 
for i in all_prime():
    print(i)