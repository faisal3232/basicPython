# method overloading in polimorphism

class A1:
    
    def myfunction(self,a,b):
        print("function with two argument")

    def myfunction(self):
        print("function with no argument")
    
    def myfunction(self,a):
        print("function with one argument")
        
    def fun(self):
        print("this is function'fun'")
 
 #creating of an object of class A1       
m=A1()

m.myfunction(33,45)


# note: method overloading is not supported in python. because python is an interpreted lnguage
# (consider last method in class  (same name) ) 
               