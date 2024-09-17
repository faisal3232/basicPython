#Multiple inheritance

class A1: #1st parentclass
    def myfunction1(self):
        print("class A1 function called")
        
class B1: #2nd parentclass
    def myfunction2(self):
        print("class B1 function called")
        
class C1(A1,B1): #child class of multiple parentclass
    def myfunction3(self):
        print("class C1 function called" )


#creating an object  of child class C1 as inheritance rule
m1=C1()    

m1.myfunction1()
m1.myfunction2()
m1.myfunction3()