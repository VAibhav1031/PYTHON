class Person:
    def __init__(self,Name,Age):
        self._Name=Name
        self._Age=Age

    @property   
    def Name(self):
        return self._Name
    
    @Name.setter
    def Name(self,Name):
        if  isinstance(Name,str) and Name:
            self._Name=Name
        
        else:
            return ValueError
        
    @property
    def Age(self):
        return self._Age
    
    @Age.setter
    def Age(self,Age):
        if isinstance(Age,int)  and Age>=0:
             self._Age=Age
        else:
            return "Age must be the non-negative number"
        

p=Person("Vaib",12)
print(p.Name)
print(p.Age)
p.Name="Girish"
print(p.Name,p.Age)
p.Age=18
print(p.Name,p.Age)
p.Age=-2
print(p.Age)



