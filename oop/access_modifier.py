#python doesnt support access modifiers by default but we use _ to signify protected and __ to signify private
# protected variables can be accessed within the same module but not from different module (garna milcha tara garna bhayena)
# private variables cannot be accessed outside the class

class Person:
    def __init__(self,name,age,password) -> None:
        self.name=name #public
        self._age=age #protected
        self.__password=password #private
        
    def get_password(self):   #indirect access of private variables
        return self.__password
        
person=Person("samp",12,"asdasda")   

# print(person.__password) # this gives error 
print(person.get_password())