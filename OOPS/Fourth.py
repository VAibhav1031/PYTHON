# Inner class demonstration

# class Outer:

#     def __init__(self):
#         self.outer_attribute="I am an Outer"

#     class Inner:

#         def __init__(self):
#             self.inner_attribute="I am Inner"


#         def innerMethod(self):
#             print("This is  an  inner method")




# outter=Outer()
# inner=outter.Inner()
# inner.innerMethod()

# ----------------------------------------

# class Student:

#     def __init__(self,name):
#         self.name=name

#     class Notebook:
#         def __init__(self,student):
#             self.owner=student.name

#         def display_owner(self):
#             print(f"The owner of the notebook {self.owner}")


# student=Student("Alice")
# nb=student.Notebook(student)
# nb.display_owner()

# ---------------------------------------


class Bank:

    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    
    class Transaction:
        def __init__(self,amount,Transaction_type):
            self.amount=amount
            self.type=Transaction_type

        def process(self,account):
            if self.type=="Deposit":
                account.balance+=self.amount
            elif self.type=="Withdraw":
                if account.balance>=self.amount:
                    account.balance-=self.amount
                else:
                    print("Insufficient Balance !!!")
    

    def makeTransaction(self,amount,Transaction_type):
        transaction=self.Transaction(amount,Transaction_type)
        transaction.process(self)
        print(f"Balance : ${self.balance}")


b=Bank("55455CD",12000)
b.makeTransaction(500,"Deposit")

