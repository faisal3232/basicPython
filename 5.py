# change the value by object

class myclass:
    def __init__(self,name,age):
        self.name= name
        self.age=age
    
    def myfunction(self):
        print(f"My name is : '{self.name}' and age is :'{self.age}'")
        print("My name is :",self.name,"and age is :",self.age)


#creating an object
m1=myclass("Faisal",30)

print(m1.name)
print(m1.age) 
m1.myfunction()

#changing the age using object

m1.age = 25
print(m1.age)
m1.myfunction()


# Delete the object
del m1.age
print("Age:",m1.age)  

 