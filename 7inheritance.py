#Multilevel Inheritance


class A: #parent class
    def myfunction(self):
        print("class A function called")
        
class B(A): #subparent class
    def myfunction2(self):
        print("class B function called")

class C(B): #child class
    def myfunction3(self):
        print("class C function called")

#creating of object of class C as inheritance rule        
m1=C()

m1.myfunction()
m1.myfunction2()
m1.myfunction3()


        
        