class Vehicle:

    def __init__(self,Type:str,Fuel:str,RegnNumber,Owner:str):
        self._Type=Type
        self._Fuel=Fuel
        self._RegnNumber=RegnNumber
        self._Owner=Owner

    @property
    def Type(self):
        return self._Type
    
    @Type.setter
    def Type(self,Type):
        self._Type=Type

    @property
    def Fuel(self):
        return self._Fuel
    
    @Fuel.setter
    def Fuel(self,Fuel):
        l=["Diesel","Petrol","Electric","Gasoline","Hydrogen"]
        if Fuel  in l:
            self._Fuel=Fuel
        else:
            print("Please enter the  valid Fuel")

    @property
    def RegnNumber(self):
        return self._RegnNumber
    
    @RegnNumber.setter
    def RegnNumber(self,j):
        self._RegnNumber=j


    @property
    def Owner(self):
        return self._Owner
    
    @Owner.setter
    def Owner(self,ow):
        self._Owner=ow
    



o=Vehicle("Bus","Diesel","5AV96OL","Harish Kumar")
print(o.Owner)
print(o.Type)
print(o.RegnNumber)
print(o.Fuel)
o.Fuel="Electric"
print(o.Type,o.RegnNumber,o.Fuel,o.Owner)
o.Fuel="Water"
print(o.Fuel)



# Basically i want  to tell you  lile getter  and setter  are the  best  method  for the  encapsulation
# getter   makes  object level variable/ instance variable  to act as a attribute 
# where  getter just make  stage 

            



    

