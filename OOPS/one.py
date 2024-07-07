class Student:
    cname="Vaibhav"
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

    def display(self): #instance method
        print("The name of the student  is :",self.name)
        print("The roll no: ",self.rollno)

    @classmethod
    def clad(cls): #Class MEthod
        print("The name of the  class  is the  ",cls.cname)

    @staticmethod
    def pun(lop):
        n_rollno=lop+1
        Student(n_rollno,"Default Name")
        return f"The next rollno {n_rollno} After {lop} Number  of the  student"


s=Student(100,"Hey ")
s1=Student(120,"Vaibhav")
s1.display()
s.display()
l=Student.pun(12)
print(l)