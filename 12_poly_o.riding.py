# method overriding in python

class MO1: # parent class
    def myfunction(self,a):
        print("class MO1 function called")
        
class MO2(MO1): # child class
    def myfunction(self,a):
        print("class MO2 function called")
        # super method calling the method of class MO1 
        super().myfunction(20)
        
class MO3(MO2):# child class 
    def myfunction(self,a):
        print("class MO3 function called")
        # super method calling the method of class MO2
        super().myfunction(10)
        
#creating an object of class MO3
m=MO3() #object of MO3

m.myfunction(10)  


        
