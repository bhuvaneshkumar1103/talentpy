'''
Create a python class called ‘Bus’ which has conductor name, total seats, seats booked, 
bus unique registration number, driver name as their properties.
'''
class Bus:
    '''
    Create member functions -
    Constructor which takes registration_name, conductor_name, driver_name, total_seats, seats_booked.
    '''
    def __init__(self, registration_num, conductor_name, driver_nmae, total_seats, seats_booked):
        self.reg_no = registration_num
        self.cond_name  = conductor_name
        self.driv_name = driver_nmae
        self.tot_seats = total_seats
        self.bookedseats  = seats_booked
        
    #print_bus_details  -> This function should print ALL details of the bus.
    def print_bus_details(self):
        print("--------------------------------------------------------")
        print("|  Bus Unique Registration Number is | ",self.reg_no)
        print("|  The Bus Driver Name               | ",self.driv_name)
        print("|  The Bus Conductor Name            | ",self.cond_name)
        print("|  The Total No of seats in the Bus  | ",self.tot_seats)
        print("|  The No of seats Booked is         | ",self.bookedseats)
        print("--------------------------------------------------------")

    #is_seat_available -> This function should return True if a seat available, if not return False.        
    def is_seat_available(self):
        if self.bookedseats < self.tot_seats:
            return True
        else:
            return False
        
    
    '''
    book_seat(no_of_seats) -> This function should book a seats if seats available, 
    else return message “Requested no of seats not available”.
    '''
    def book_seats(self,no_of_seats):
        seat_available = self.tot_seats - self.bookedseats
        if seat_available > no_of_seats :
            self.bookedseats += no_of_seats
            return "The Given no of seats are booked "
        else:
            return "Requested no of seats not available"
#Object1 for the class Bus which gives the required arguments to the Bus class functions.        
p1 = Bus("TN101", "Joe", "John", 25, 12)
#calling the respective functions in the class Bus with object p1.
p1.print_bus_details()
print(p1.is_seat_available())
print(p1.book_seats(1))
print(p1.book_seats(2))
print(p1.book_seats(21))

#Object2 for the class Bus which gives the required arguments to the Bus Class functions.  
p2 = Busobj = Bus("TN102", "Britto",  "Prince", 100, 100)
p2.print_bus_details()
print(p2.is_seat_available())
print(p2.book_seats(1)) 

'''
Output:
    --------------------------------------------------------
    |  Bus Unique Registration Number is |  TN101
    |  The Bus Driver Name               |  John
    |  The Bus Conductor Name            |  Joe                 -> displaying the Bus details.
    |  The Total No of seats in the Bus  |  25
    |  The No of seats Booked is         |  12
    --------------------------------------------------------
    True                                                        -> If the seats are available in the Bus.     
    The Given no of seats are booked                            -> The requested no of seats are booked.
    The Given no of seats are booked                            -> The requested  no of sears are booked.
    Requested no of seats not available                         -> The requested no of seats are not available in the bus.
    --------------------------------------------------------
    |  Bus Unique Registration Number is |  TN102
    |  The Bus Driver Name               |  Prince 
    |  The Bus Conductor Name            |  Britto              -> displaying the Bus details.
    |  The Total No of seats in the Bus  |  100
    |  The No of seats Booked is         |  100
    --------------------------------------------------------
    False                                                       -> If the seats are not available in the Bus.
    Requested no of seats not available                         -> The requested no of seats are not available in the bus.
'''