'''
generator which will give the output as even numbers from 1 to infinity.
'''
def all_even():       
    n = 0
# to create a infinity loop .
    while True:
# it will yield only the even numbers
        if n%2 == 0:
            yield f'{n} is even' 
        n += 2
for i in all_even():
    print(i)
