# achieveing encapsulation by private

class A: # parent class
    def __init__(self,a):
        self.__a # the variable is a private variable
        
    def show(self):
        # printing a private variable using function
        print("private variable : ",self.__a)
        
        
class B(A): # child class
    def __init__(self,b):
        super().__init__(b)
        
    def showB(self):
        # printing a private variable using function
        print(self.__a)

# creating an object of child class

obj=B(20)    
obj.showB    