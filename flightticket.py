'''
Mr. Ashok like to create a flight ticket booking application. To book a
flight, user should enter his / her name, DOB, address and passport
number followed by Start city, destination city and date of travel. Here are
the constraints -
1. Name should be all in upper case and it should be free from special
characters or numbers. His application only allow names of length
ranges from 5 to 30 max.
2. DOB should be in a format of DD-MM-YYYY. Other formats not
allowed.
3. Passport number is only of 8 digits and should start with ‘P’
followed by numbers.
4. Start city and destination city should NOT be same. Here are the
constraints -
1. Start city / End city should be any one of these [ “Paris”,
“Japan”, “China”]
5. Date of travel should be in format [DD-MM-YYYY]
Write functions to validate all those above constraints and if all validations
successful, return “Flight Ticket Booked”, else return respective error
message. (Example: Invalid Passport number if passport number validation
fails etc….)
'''
def name_validator(name):
    invalidcharacters=['1','2','3','4','5','6','7','8','9','0','"',"'",'/','\\','!','@','#','$','%','^','&','*','(',')','-','_','+','=','[','{','}',']',':',';','|','<','>',',','.','?','`','~']
    if name.isupper() == False:
        return False
    for i in name:
        if i  in invalidcharacters:
            return False
    if len(name)<5 or len(name)>30:
        return False

    return True

def date_validator(date):
    nums=['1','2','3','4','5','6','7','8','9','0']

    if len(date)!=10:
        return False

    if date[0] not in nums or date[1] not in nums or date[3] not in nums or date[4] not in nums or date[6] not in nums or date[7] not in nums or date[8] not in nums or date[9] not in nums:
        return False

    if date[2]!='-' or date[5]!='-':
        return False

    return True

def passportnumber_validator(passnum):
    nums=['1','2','3','4','5','6','7','8','9','0']
    if len(passnum)!=8:
        return False
    if passnum[0]!='P':
        return False
    for i in range(1,8):
        if passnum[i] not in nums:
            return False
    return True

def city_validator(start,destination):
    valid_cities=['Paris','Japan','China']

    if start == destination:
        return False

    if start not in valid_cities or destination not in valid_cities:
        return False

    return True
def ticket_validator(name,dob,passport_number,start,destination,date_of_travel):

    flag=1

    if name_validator(name)==False:
        print('Invalid Name')
        flag =0
        
    if date_validator(dob)==False:
        print('Invalid DOB')
        flag =0

    if passportnumber_validator(passport_number)==False:
        print('Invalid Passport Number')
        flag =0

    if city_validator(start,destination)==False:
        print('Invalid City')
        flag =0

    if date_validator(date_of_travel)==False:
        print('Invalid Date Of Travel')
        flag =0

    if flag==1:
        print('Flight Ticket Booked')

name = str(input("Enter Your name in uppercase:"))
dob  = str(input("Enter Your Date of Birth  in DD-MM-YYYY Format:"))
passport_number = str(input("Enter Your Passport Number:"))
start = str(input("Enter Your Start City:"))
destination = str(input("Enter Your Destination City:"))
date_of_travel = str(input("Enter Your Date of Travel in DD-MM-YYYY:"))
    
ticket_validator(name,dob,passport_number,start,destination,date_of_travel)        
    
