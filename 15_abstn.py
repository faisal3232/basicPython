# Abstraction


class animal: # abstract class
    #def move(self): # abstract method 
     #   pass
     X="HELLO"

class dog(animal):
    def move(self): # class animal implements method here
        print("i can bark") 
             
class snake(animal):
    def move(self): # class animal implements method here
        print("i can hisss")
        
#creating an object of class dog

m=dog()

#creating an object of class dog

m1=snake()

m.move()
m1.move()
