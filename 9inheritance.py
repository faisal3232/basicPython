#hierarchical inheritance

class A1: #parent class
    def myfunction1(self):
        print("class A1 function called")
        
class B1(A1): #child class 
    def myfunction2(self):
        print("class B1(child1) function called")
        
class B2(A1): #child class 
    def myfunction3(self):
        print("class B2(child2) function called")
        
m2=B1()
m3=B2()

m2.myfunction1()#function of class A1
m3.myfunction1()#function of class A1
m2.myfunction2()
m3.myfunction3()

        