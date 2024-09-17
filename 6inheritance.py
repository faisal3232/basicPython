# single inheritance

class parentclass:
    def myfunction1(self): # parent class property
        print("parent class function called")
        
class childclass(parentclass): #child class which inherit parentclass & writing parent class in () to inherit
    def myfunction2(self): # child class property
        print("child class function called")
        
#you have to create childclass"s object according to inheritance rule

#creating an object of child class

c1=childclass()
c1.myfunction1()
c1.myfunction2() 

