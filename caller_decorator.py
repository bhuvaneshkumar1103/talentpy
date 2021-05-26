'''
it  is a decorator in which it will call the function which is passed has the 1st parameter
untill n times, the n is the 2nd parameter. 
'''
def perform_n_calls(function,N):
    def caller():
        for i in range(N):
            function()
    return caller()    
        


        
