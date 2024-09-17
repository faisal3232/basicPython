# achieveing encapsulation by protected
class A: # parent class
    def __init__(self,a):
        self._a = a # the variable is a protected variable
        
    def show(self):
        # printing a protected variable using function
        print("private variable : ",self._a)
        
class B(A): # child class
    def __init__(self,b):
        super().__init__(b)
        
    def showB(self):
        # printing a private variable using function
        print("variable value : ",self._a)
        #super().show()    
        
# creating an object of child class

obj=B(20)    
obj.showB()    
