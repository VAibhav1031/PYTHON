# print("PROBLEM 1!!")
# print("SOLUTION::\n")
# class Line:

#     def __init__(self,coor1,coor2):
#         self.coor11=coor1
#         self.coor2=coor2

#     def distance(self):
#         x1,y1=self.coor11
#         x2,y2=self.coor2

#         return((x2-x1)**2+(y2-y1)**2)**0.5
    

#     def slope(self):
#         x1,y1=self.coor11
#         x2,y2=self.coor2

#         if(x2-x1==0):
#             return "undefined"
        
#         else:
#             return (y2-y1)/(x2-x1)

# coordinate1=(3,2)
# coordinate2=(8,10)

# li=Line(coordinate1,coordinate2)

# print(li.distance())
# print(li.slope())
        
# print("----------------------------------")
# print("problem 2 SOLUTION:\n")
# # problem 2:

# class cylinder:

#     def __init__(self,height=1,radius=1):
#         self.height=height
#         self.radius=radius

#     def volume(self):
#         return self.height*self.radius**2*3.14
    
#     def area(self):
#         return (self.height*self.radius*3.14*2)+(self.radius**2*3.14*2)
    

# c=cylinder(2,3)

# print(c.volume())
# print(c.area())
    
# print("----------------------------------")
# print("CHALLENGE PROBLEM!!\n")
# print("PROBLEM SOLUTION::\n\n")


class account:

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposits(self,deposits):
        self.balance=self.balance+deposits
        return f"${deposits} Deposit Accepted"
    
    def withdraw(self,withdraw):
        if(withdraw>self.balance):
            return "Funds Unavailable!"
        else:
            self.balance=self.balance-withdraw
            return f"${withdraw} Withdrawal Accepted"
        
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

        
acct1 = account('Vaibhav',4500)


print("WELCOME TO TIWARI-BANK ATM!!")
print("SELECT OPTION FOR SERVICES :")
print("1. ACCOUNT BALANCE")
print("2. WITHDRAWL")
print("3. DEPOSITS")
ch='y'


while(ch=='y'):
    n=int(input("Enter your choice:"))    
    if(n==1):
        print(acct1)
    elif(n==2):
        witd=int(input("Enter the withdraw amount:"))
        print(acct1.withdraw(witd))
        print("\n")
        print(acct1)
    elif(n==3):
        dip=int(input("Enter the deposit amount:"))
        print(acct1.deposits(dip))
        print("\n")
        print(acct1)

    else:
        print("INVALID CHOICE")
        print("TRANSACTION CANCELLED!! :( ")

    ch=input("WANT  TO  AVAIL ANOTHER SERVICES? Y/N")
    


