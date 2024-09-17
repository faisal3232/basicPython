# Hybrid inheritance

class A1 : # parentclass
    def myfunction1(self):
        print("class A1 function called")
        
class B1(A1) : # subparentclass1
    def myfunction2(self):
        print("class B1 function called")
        
class B2(A1) : # subparentclass2
    def myfunction3(self):
        print("class B2 function called")
        
class C1(B1,B2) : # childclass
    def myfunction4(self):
        print("class C1 function called")
 
m1=C1()
 
m1.myfunction1()

m1.myfunction4()     
m1.myfunction3()     
m1.myfunction2()              