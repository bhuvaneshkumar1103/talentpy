#creat a class doctor to have the details about the doctor.
class Doctor:
    def __init__(self, doctor_name, specialisations, avalability_days, appointment_seat, hospital):
        self.doctor_name = doctor_name
        self.specialisations = specialisations
        self.availability_days = avalability_days
        self.appointment_seat = appointment_seat
        self.hospital = hospital
    
    #This method is to check the doctor's availability on the particular day.    
    def is_available(self,day):
        if day in self.availability_days and self.appointment_seat[day]>0:
            return True
        else:
            return False 
    
    #This method is to check whether the doctor is an specialist at requested disease.
    def is_specialist(self,disease):
        if disease in self.specialisations:
            return True
        else:
            return False
    #This method willcheck whethe a appointment can be made on the requested day.
    def book_appointment(self,day,disease):
        
        if self.is_specialist(disease) == False:
            return -1
        if self.is_available(day) == False:
            return 0
        else:
            return 1
    #This method will book the appointment on the requested day.
    def do_booking(self,day, disease):
        if self.book_appointment(day,disease) == -1:
            return str("\n Requested Doctor is not a specialist for your request")
        elif self.book_appointment(day,disease) == 0:
            return str("\n Doctor is not available on your requested day")
        elif self.book_appointment(day,disease) == 1:
            self.appointment_seat[day] -= 1
            print("\n 1. Doctor Name : ", self.doctor_name)
            print("\n 2. Hospital Name : ",self.hospital.hospital_name)
            print("\n 3.Addresss : ",self.hospital.hospital_address)
            print("\n 4.Patient Name :", patient.Patientname)
            print("\n 5.Booking Day :", day)
            print("\n 6.Booked for :", disease)
            return str("\n Appointment Successful")
        
#Create a class to have the details of the Hospital.    
class Hospital:
    def __init__(self,hospital_name, hospital_address):
        self.hospital_name = hospital_name
        self.hospital_address = hospital_address

#Create a class to have the details of the Patient.        
class Patient:
    def __init__(self,name_of_patient, disease, assigned_doctor):
        self.Patientname = name_of_patient
        self.disease = disease
        self.assigned_doctor = assigned_doctor
        
    #This method will start the booking process.    
    def book(self,requested_day):
        print(self.assigned_doctor.do_booking(requested_day, self.disease))
        
hospital = Hospital("ABC Multi-speciality Hospital","71, South Street, Ambattur, Chennai")
doctor = Doctor("Dr. John", ["Diabetics", "ENT"], ["Monday", "Friday"], {"Monday" : 5, "Friday" : 1}, hospital)
patient = Patient("talentpY", "Diabetics", doctor)
patient.book("Friday")
patient.book("Friday")
patient.book("Tuesday")

patient = Patient("Roy", "Dengue", doctor)
patient.book("Monday")

'''
Output:

 1. Doctor Name :  Dr. John

 2. Hospital Name :  ABC Multi-speciality Hospital

 3.Addresss :  71, South Street, Ambattur, Chennai

 4.Patient Name : talentpY

 5.Booking Day : Friday

 6.Booked for : Diabetics

 Appointment Successful

 Doctor is not available on your requested day

 Doctor is not available on your requested day

 Requested Doctor is not a specialist for your request
'''