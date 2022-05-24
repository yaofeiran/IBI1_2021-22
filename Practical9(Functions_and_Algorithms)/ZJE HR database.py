#create a class named "Staff"
class Staff(object):
    def __init__(self,first_name,last_name,location,role):
        self.first_name=first_name#input("First name:")
        self.last_name=last_name#input("Last name:")
        self.location=location#input("location(Edinburgh or International campus):")
        self.role=role#input("role:")

    #def information(self):
        print("Staff:",self.first_name,self.last_name,"location:",self.location,"role:",self.role)

#eg:
Staff("Shuping","Zhang","International campus","faculty")




        
