# Abstraction

class RBI: # Abstract class 
    def interest(self): # Abstract method
        pass
            
class SBI(RBI): #child class 
        def interest(self): # RBI interest method implements here
            print("SBI interest is 5%")

class HDFC(RBI):#child class
    def interest(self): #RBI interest method implements here
        print("HDFC interest is 2%")
    
#creating an object of class SBI
s=SBI()

#creating an object of class HDFC
h=HDFC()

s.interest() # SBI interest method called

h.interest() # HDFC interest method called
 


