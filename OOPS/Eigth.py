class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):

        """
        RETURNS:
            Points: New Point object returns the sum"""
        return Point(self.x+other.x,self.y+other.y)

    
    def __truediv__(self,other):

        return Point(self.x/other,self.y/other)
    

    def __mul__(self,other):

        """
        Returns:
            Points :  A new  point  object  will return the  multiplaction of the two obejct"""
        # return Point(self.x*other.x,self.y*other.y)
        return Point(self.x*other,self.y*other)

    def area(self):
        return self.x*self.y
    
    def __eq__(self, other: object) -> bool:

        """
        compares two area of the  rectangles
        Returns:
           bool: returns  True if both  area of  rectangles are same , other wise False
           """  
        return self.area()==other.area()
    

    def __lt__(self,other):
        """
         Compares two Rectangle objects using the < operator.
        Returns:
            bool: returns  True if this area of  rectangles is smaller than other, other wise False
        """
        # return self.area()<other.area()
        return (self.x<other.x,self.y<other.y)   #we can use  both way for implementation of less than operator  on method's  or particular object(instance)variable
    
    

    def __le__(self,other):
        """
         Compares two Rectangle objects using the <= operator.
        Returns:
            bool: returns  True if this area of  rectangles is smaller than other, other wise False
        """
        return self.area()<=other.area()
    

    def __repr__(self) -> str:
        return f"Point(f{self.x},{self.y})"
    
    


p1=Point(3,4)
p2=Point(1,2)


print("Checking Equality in Area : ",p1==p2)
print("less than ",p2 < p1)
print("Multiplication : ",p1*2)
print("Division",p1/2)

    


