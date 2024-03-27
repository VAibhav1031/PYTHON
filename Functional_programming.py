# # Map

# def square(number):
#     return number**2

# numbers=[2,5,8,9,10]
# sq=map(square,numbers)
# print(list(sq))


# # Converting  the string to int   in the list

# l_num=["4","5","8","5","8"]
# int_num=map(int,l_num)
# l=list(int_num)
# print(l)

# # can convert  between the built-in  datatype

# # to float
# print("Map:Float function")
# l_=[4,5,-5,1,2,3]
# int_num=map(float,l_)
# l=list(int_num)
# print(l)
# print()

# # with absolute
# print("Map:Abs function")
# int_num1=map(abs,l_)
# l=list(int_num1)
# print(l)
# print()

# # with len function
# print("Map:len function")
# ch=["welcome","hey","Real","python"]
# int_num2=map(len,ch)
# l=list(int_num2)
# print(l)

# # Lambda also can be uses  to uses in-hand expression based function:

# num=[2,5,6,8,10,11]
# sq=map(lambda x :x**2,num)
# lis=list(sq)
# print(lis)

# # multiple input
# first_it=[1,2,3]
# sec=[4,5,6,7]
# print(list(map(pow,first_it,sec)))

# print(list(map(lambda x,y:x-y,[2,4,6],[1,3,6])))


# #TRansforming iterable of strings with  python map()

# # Method of str

# st=["processing","strings","with","map"]
# print("Capitalize")
# print(list(map(str.capitalize,st)))
# print()

# print("Upper")
# print(list(map(str.upper,st)))
# print()

# print("lower")
# print(list(map(str.lower,st)))
# print()

# # If you need to supply arguments rather than rely on the default value,
# # then you can use a lambda function.

# print("Removing strip  leading or late strip")
# with_dots = ["processing..", "...strings", "with....", "..map.."]
# print(list(map(lambda s:s.strip("."),with_dots)))




# # Ceasar  Algorithm

# def encr(c):
#     rot_by=3
#     c=c.lower()
#     alp="abcdefghiklmnopqrstuvwxyz"
#     if c not in alp:
#         return c
    
#     rotated=ord(c)+rot_by

#     # if the rotation is inside the alphabet
#     if rotated<=ord(alp[-1]):
#         return chr(rotated)
    
#     # if the rotation goes beyond the alphabet
#     return chr(rotated-len(alp))

# print("".join(map(encr,"My secret message goes here")))




# # Join method used in the string
# #->The .join() method in Python is used to concatenate elements of an iterable,
# #  such as a list, tuple, or string, into a single string. It joins together the 
# # elements of the iterable using a specified separator and returns the concatenated string.

# # Joining a list of strings:
# words=["Hello","world","from","python"]
# re=" ".join(words)
# print(re)
# print()

# # joining a list of numbers converted to strings:
# word="Python"
# re="-".join(word)
# print(re)
# print()

# # Joining using an empty  as sperartor:

# words=["apple","banana","Orange"]
# re="".join(words)
# print(re)
# print()

# # joining a list of wors with a comma and space separator
# words=["apple","banana","orange"]
# result=", ".join(words)
# print(result)
# print()

# # Joining the  list of integer  into  a  string  by converting them
# num=[2,5,8,6,3]
# result=" ".join(str(n) for n in num)
# print(result)
# print()

# # joining characters of string with a space separator:
# word="Python"
# re=" ".join(word)
# print(re)
# print()

# # Joining elements of  dictionary's keys with  a comma and space separator
# my_dict = {"name": "John", "age": 30, "city": "New York"}
# result = ", ".join(my_dict.keys())
# print(result)
# print()


# # Map: Using math operator
# num=[2,5,8,6,9,2]
# re=list(map(lambda x:(x**2,x**2),num))
# print(re)


# # Factorial
# import math

# num=[2,5,8,15]
# print(list(map(math.factorial,num)))
# print()

# cels_temp=[100,40,80]
# fah_temp=[100.0,40.0,80.0]

# c_l_to_f=list(map(lambda x:9/5*x+32,cels_temp))
# print(c_l_to_f)
# print()

# f_l_to_c=list(map(lambda x :(x-32)*5/9,fah_temp ))
# print(f_l_to_c)


# # if you are not  sure that  your data is clean
# def to_float(num):
#     try:
#         return float(num)
#     except ValueError:
#         return float("nan")
# print(list(map(to_float,["12.3","3.3","-15.2","one"])))
    


# ******Filter**********
# Sometimes you need to process an input iterable and return another iterable that results from filtering out 
# unwanted values in the input iterable. In that case, Python’s filter() can be a good option for you. filter() is a built-in function
# that takes two positional arguments:

# function will be a predicate or Boolean-valued function, a function that returns True or False according to the input data.
# iterable will be any Python iterable.
# filter() yields the items of the input iterable for which function returns True. If you pass None to function, then filter() uses the identity function. This means that filter() will check the truth value of each item in iterable and filter out all of the items that are falsy.


# see this --
# >>> import math

# >>> math.sqrt(-16)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#     math.sqrt(-16)
# ValueError: math domain error

# With a negative number as an argument, math.sqrt() raises a ValueError. To avoid this issue,
# you can use filter() to filter out all the negative values and then find the square root of the remaining positive values.


# import math 

# def is_positive(number):
#     return number >=0

# def sanitized_sqrt(num):
#     s=map(math.sqrt,filter(is_positive,num))
#     return list(s)


# print(sanitized_sqrt([25,9,81,-16,0]))





# *****Functions*************:

# # WAPF that invokes a function after a specified  period of time
# # Sample Output:
# # Square root after specific miliseconds:
# # 4.0
# # 10.0
# # 158.42979517754858


# from time  import sleep
# import math

# def delay(fn,ms,*args):
#     sleep(ms/1000)

#     return fn(*args)

# print("Square root  after  specific milliseconds")
# print(delay(lambda x:math.sqrt(x),100,16))


# # Detect  the number of local variables in the function

# def fun():
#     x=2
#     ba='is there'
#     li=[2,5,8,9,6]

#     print("hey there")

# print(fun.__code__.co_nlocals)

# # WAPF  to  access a  function  inside  a  function
# def func(n):
  
#     def add(b):
#         return n+b
        
#     return add

# print(func(5))
            


# # WAPF to execute the  code in the string
# mi="print(\"hello world\")"
# exec(mi)


# # WAPF  to create and print a list  where the values are the square  of numbers
# # betweeen the  1 and 30 (both included)


# def lis():
#     n=30
#     re=[]
#     for i in range(1,n+1):
#         re.append(i**2)

#     print(re)

# lis()


# # WAPF that  accepts  a  hyphen-separated sequence of words  as input
# # and prints  the  words  in  hyphen-separated sequence after sorting them 
# # alphabetically

# # Sample Items : green-red-yellow-black-white
# # Expected Result : black-green-red-white-yellow

# def sor(inp):
#     p=inp.replace("-"," ")
#     p_l=p.split()
#     l=sorted(p_l)
#     return "-".join(l)

# print(sor("green-red-yelloe-black-white"))



# # WAPF to check  whether a  string  is  a pangram  or not 
# import string
# def pangram(st):
#     s=st.lower()

#     for letter in string.ascii_lowercase:
#         if letter not in s:
#             return False
        
#     return True

# sentence="The quick brown fox jumps  over the lazy dog."
# print(pangram(sentence))



# # Check the  perfect  number or not
# def perfect(num):
#     l=[]
#     for i in range(1,num):
#         if num%i==0:
#             l.append(i)
#     if sum(l)==num:
#         return "Perfect number"
    
#     return False

# n=int(input("Enter the number : "))
# print(perfect(n))


# # check prime
# import math
# def Prime_check(n):
#     if n<2:
#         return "prime number is greater than 1"
    
#     else:
#         for i in range(2,int(math.sqrt(n))+1):
#             if n%i==0:
#                 return False
            
#         return True
# print(Prime_check(5))



#**********Lambda**********question****
# # 1
# r=lambda s : s+15
# print(r(10))

# r=lambda x,y:x*y
# print(r(4,4))

# # 2

# k=lambda s:s*2
# k1=lambda s:s*3
# k2=lambda s:s*4
# k3=lambda s:s*5

# print("Double the number 15 = ",k(15))
# print("triple the number 15 = ",k1(15))
# print("Quadruple the number 15 = ",k2(15))
# print("Quintuple the number 15 = ",k3(15))


# # 3
# subjects_marks=[("English",88),("science",90),("Maths",97),("Social Science",82)]

# print("Original list of tuples : ")
# print(subjects_marks)

# subjects_marks.sort(key=lambda x:x[1])

# print("\n sorting the list of the tuples")
# print(subjects_marks)

# # 4
# l=[1,2,3,4,5,6,7,8,9,10]
# eve=list(filter(lambda s:s%2==0,l))
# print(eve)

# od=list(filter(lambda s:s%2!=0,l))
# print(od)

# # 5
# org=[1,2,3,4,5,6,7,8,9,10]
# l=list(map(lambda x:x**2,org))
# print(l)
# l1=list(map(lambda x:x**3,org))
# print(l1)
# l2=list(map(lambda x:x**4,org))
# print(l2)

# # 6
# starts_with=lambda x: True if x.startswith("P") else False
# print(starts_with('Python'))

# # 7
# import datetime

# s=datetime.datetime.now()
# print(s)
# D=s.year
# M=s.month
# Y=s.day
# S=s.time()

# print(D)
# print(M)
# print(Y)
# print(S)

# # 8
# org=[-1, 2, -3, 5, 7, 8, 9, -10]
# l=list(filter(lambda x:x>0,org))
# l1=list(filter(lambda x:x<0,org))
# f=l+l1
# print(f)
# print(sorted(org))

# # 9 WAPP to count the even and odd numbers in a given array of integers using Lambda.
# oo=[1,2,3,5,7,8,9,10]
# od=list(filter(lambda x: x%2!=0,o))
# print(od)

# eve=list(filter(lambda x:x%2==0,o))
# print(eve)



# # 10 WAPP to add given  lists using map  and lambda

# l1=[1,2,3]
# l2=[4,5,6]

# l=list(map(lambda x,y:x+y,l1,l2))
# print(l)


# #11 WAPP to match the pallindrome in the list
# o_=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

# l=list(map(lambda x:x[::-1]==x,o_))
# print(l)

# # so this  will give you  True  and  False according to the  condtion

# # so we are  gonna use  filter here

# l=list(map(lambda x:x,filter(lambda x:x[::-1]==x,o_)))
# print(l)


# #12 WAPP to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda. Input the number of students, the names and grades of each student.
# # Input number of students: 5
# # Name: S ROY
# # Grade: 1
# # Name: B BOSE
# # Grade: 3
# # Name: N KAR
# # Grade: 2
# # Name: C DUTTA
# # Grade: 1
# # Name: G GHOSH
# # Grade: 1
# # Names and Grades of all students:
# # [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
# # Second lowest grade: 2.0
# # Names:
# # N KAR


# # solution:

# k=int(input("Input the number of students: "))
# m=[]
# for i in range(k):
#     r=[]
#     n=input("Name: ")
#     g=int(input("Grade: "))
#     r.append(n)
#     r.append(g)
#     m.append(r)

# print(m)


# min_grade=min(student[1] for student in m)

# m=[student for student in m if student[1]!=min_grade]

# second_min_grade=min(student[1] for student in m)


# print("second lowest grade : ",second_min_grade)
# print("Name")

# for student in  m:
#     if student[1]==second_min_grade:
#         print(student[0])



# # WAPP  to  find all anagrams of a string in a given list of string using lambda

# # Orginal list of strings:
# # ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# # Anagrams of 'abcd' in the above string:
# # ['bcda', 'cbda', 'adcb']


# strin=['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# target="abcd"

# is_anagram=lambda s1,s2:sorted(s1)==sorted(s2)

# an=list(filter(lambda s:is_anagram(s,target),strin))
# print(an)


# # WAPP  that sums the length of a list of names after removing those that start with lowercase letters. Use the lambda function.

# sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']

# sample_name=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))

# n=len("".join(sample_name))
# print(n)


# #  Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda.
# #Original Dictionary:
# # {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# # Height> 6ft and Weight> 70kg:
# # {'Cierra Vega': (6.2, 70)}


# l={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}

# k=dict(filter(lambda d : (d[1][0],d[1][1])>(6.0,70),l.items()))

# print(k)


# # WAPP to check whether a specified list is sorted or noy uding lambda.
# # Original list:
# # [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# # Is the said list is sorted!
# # True
# # Original list:
# # [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# # Is the said list is sorted!
# # False

# orf=[1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# nums2 = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

# def check_sor(li):
#     if li==sorted(orf):
#         return True
    
#     return False

# print(check_sor(orf))
# print(check_sor(nums2))


# # WAPP to extract the  nth element from a given list of tuples

# # [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# # Extract nth element ( n = 0 ) from the said list of tuples:
# # ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
# # Extract nth element ( n = 2 ) from the said list of tuples:
# # [99, 96, 94, 98]


# p=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# def ext(l,n):
#     return list(map(lambda x:x[n],l))

# print(ext(p,1))

# # list compression
# n=int(input("Input the nth element index"))
# f=[x[n] for x in p]
# print(f)


