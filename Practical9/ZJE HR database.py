#create a class named "Staff"
class Staff(object):
#attributes of the staff,containing first and last name, location and role
    #attributes are set when the marker input 
    first_name=input("First name:")
    last_name=input("Last name:")
    location=input("location(Edinburgh or International campus):")
    role=input("role:")
#creat a function printing the staff's information in a single line
    def information(self):
        print("Staff:",self.first_name,self.last_name,"location:",self.location,"role:",self.role)

#create an object staff1
staff1=Staff()
#call the method
staff1.information()

        
