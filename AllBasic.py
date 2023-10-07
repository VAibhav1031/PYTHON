# mylist=[1,2,5,8,6,3,8,28,45]
# for num in mylist:
#     print (num)


# for  jelly in mylist:
#     if jelly%2==0:
#         print("Even")

#     else:
#         print("Odd")


# myl=[(5,6,9),(5,9,10),(7,4,1)]
# for a,b,c in myl:
#     print(a)

# dict={"key1":1,"key2":2,"key3":3}
# for key,value in dict.items():
#     print(key)
# #     print(value)

# x=0
# while x<5:
#     print(f"the current value of the x is {x}")
#     x=x+1

# mystring="vaibhav Tiwari"

# for i in mystring:
#     if(i=="a"):
#         continue
#     print(i)

# print("helllo there is something i want to {}".format("insert"))
# print("hey ther is {0} {2} {1}".format("quick","fox","brown"))
# print("hey ther is {b} {f} , it is very  {q}".format(q="quick",f="fox",b="brown"))

# l="live"
# print(f" my name is vaibhav Tiwari where do you {l} ")
# str="helllo there is something i want to {}"
# print(str.format("insert"))

# str_="hey there!1"
# x=0
# i=len(str_)
# while x<len(str_):
#     if(str_[i]=="e"):
#         continue
#     print(x)

#     x+=1

# mynum=[2,5,"hey"]
# for num in  mynum:
#     # here the  pass is used to avoid the  
#     # return of error if we don't  know what to do in his
#     pass  

# print("hey there man whatsupp!!!")

# here the break statement is used to  break  the  loop  or you 
# can use it  where you want  the  result from your loop see below  example

# x=0
# while x<5:
#     if(x==2):
#         break
#     print(x)
#     x+=1

# you see i just  want  to print  upto  1 so use brea statement to breal
# the loop upto that  iteration

# word="vaibhav"
# i=0
# for  item in word:
#     print(item)

# word="vaibhav"
# for item in enumerate(word):
#     print(item)
# here  enumerate is been used to unpack the  string with its index
# there are many other methods to

# word="vaibhav"
# for index,value in enumerate(word):
#     print(index)
#     print(value)
#     print("\n")


# similarly here we have the  zip method  where we do same thing like enumberate
# but in the  zip we have to  zip  the thing  first then can use  that thing like enumeration

# example1:
# mylist1=[1,2,3]
# mylist2=["a","b","c"]

# for item in zip(mylist1,mylist2):
#     print(item)

# we cAN  do  as much zip  we  want  to do
# mylist1=[1,2,3]
# mylist2=["a","b","c"]
# mylist3="hey"

# for item in zip(mylist1,mylist2,mylist3):
#     print(item)

# we can  zip  of  any datatype  not  only for the  list you can use string  and etc

# zip and  enumeration is same  but in zip you hav to  zip them  but  that not  the case with enumeration


# here it comes the list comprehensions
# mystring="hello"
# mylist=[]

# for letter in mystring:
#     mylist.append(letter)

# print(mylist)

# so here we us the  list append  function to  make the empty list  to fill one by one
# character of string  in append mode

# here comes  more in the thing
# mylist=[letter for letter in "vaibhav Tiwari"]
# print(mylist)
# # so here  we can   create it  very easily without  using the list loop

# mylist2=[num*2  for num in range(0,11)]
# print(mylist2)

# # here it is also another method  we can create the thing:
# mylist3=list("hello")
# print(mylist3)

# we can make it more  complex

# celcius=[0,20,-10,35,40,50]
# # the  formula of conversion c to °F = (9/5) °C+32
# # so here we iterate the celcius  using temp variable one by one
# fahrenheit=[((9/5)*temp+32) for temp in celcius]
# print("So here we get the conversion from the celcius to fahrenheit")
# print(fahrenheit)

# sum=0
# mylist=[495, 1013, 911, 1102 ,974, 158 ,768, 207, 583 ,683 ,1295 ,533, 473, 949, 918, 385, 842, 184 ,794, 1271, 660, 844, 157 ,215, 1223, 663, 1090 ,313 ,407, 1253 ,779, 821 ,1242 ,1017, 1282 ,1276 ,933 ,1038 ,668, 539 ,1041]
# for i in range(len(mylist)):
#     sum+=mylist[i]
    
# print(sum)

# def check_even(num_list):
#     for number in num_list:
#         if number%2==0:
#             return True
        
#         else:
#             pass

#     return False
    

# list_=[1,5,6,3,4,25]
# print(check_even(list_))

# # if  i have  to return  a even number list only  we have  to remove  the  true  an d false

# def check_even(num_list):
#     even_list=[]
#     for number in num_list:
#         if number%2==0:
#             even_list.append(number)
#         else:
#             pass
    
#     print(even_list)

# list=[25,6,34,29,6,48,12,57,5]
# check_even(list)

# tupple unpacking
# stockprices=[("APPL",200),("GOOG",400),('MSFT',100)]

# for item in stockprices:
#     print(item)

# #  simple unpacking
# for ticker,price in stockprices:
#     print(ticker)

# print("\n")

# for ticker,price  in stockprices:
#     print(price+(price*0.1))
#     # 10% increase in the price of stock

# Now  we are gonna use the function to unpac the  complex thing out

# so  see  here  is the  example  we have the list of the tuples and 
# we have  to select the employee of the  month  by  it   how much he worked in hourss

# work_hours=[("cassei",150),("vaibhav",5000),("harish",360),("Rana",650),("vivek",160),("mahesh",680),("jaadu",567)]

# def employee_check(work_hours):
#     current_max=0
#     employee_of_month=""

#     for employee,hours in work_hours:
#         if hours>current_max:
#             current_max=hours
#             employee_of_month=employee

#         else:
#             pass

#     return(employee_of_month,current_max)


# print(employee_check(work_hours))

# # hey there 
# example=[1,2,3,4,5,6,7]

# from random import shuffle
# shuffle(example)

# print(example)
# from random import shuffle

# def player_guess():
#     guess = ''

#     while guess not in ['0', '1', '2']:
#         guess = input("Pick a number between 0, 1, and 2: ")

#     return int(guess)

# mylist = [' ', 'O', ' ']

# # Shuffle the list in place
# shuffle(mylist)

# guess = player_guess()

# def check_guess(mylist, guess):
#     if mylist[guess] == 'O':
#         print("Correct!!")
#     else:
#         print("Wrong Answer")
#         print(mylist)

# check_guess(mylist, guess)


# today  there  will something  different 

##def myfunc(a,b):
##    return sum((a,b))*0.05
##
##print(myfunc(40,52))
##
### to use or pass  as many arguments you have to use the *args
##
##def myfunc_(*args):
##    return sum(args)*0.05
##
##
##def myfunc1(**kwargs):
##    print(kwargs)
##    #here vegie acts as a key in dictionary
##    if "Vegie" in kwargs:
##        print("my  fruit of  choice is {} ".format(kwargs["Vegie"]))
##
##    else:
##        print("i dont know ")

## here  wee gobnna  use both kwargs and args

##def func(*args,**kwargs):
##    print(args)
##    print(kwargs)
##    print("i would  like {} {}".format(args[0],kwargs["animal"]))



##def myfunc(*args):
##
##    mylist=[]
##    for i in args:
##        if i%2==0:
##             mylist.append(i)
            
##    return mylist


# def fu(*args):
#     mylist=list(args)
   

#     eve_lst=[]
#     for i in mylist:
#         if i%2==0:
#             eve_lst.append(i)

#     return eve_lst
            
# QUESTION 1 :>LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# #  hello here  we  gonna  make new function  in which  we have  to chec
# # the two  even which one  is  smaller

# # sol1
# def lesser_of_two_evens(a,b):
    
#     if(a%2==0 and b%2==1):
#         if (a>b):
#             return a
#         else:
#             return b
        
#     elif(b%2==0 and a%2==1):
#         if (a>b):
#             return a
#         else:
#             return b
#     else:
#         if(a%2==0 and b%2==0):

#             return min(a,b)

# a=int(input("Enter the  even number a:"))    
# b=int(input("Enter the  even number b:"))  
# print(lesser_of_two_evens(a,b))

# #  so  i completed what my  question is  asking to do  to  return the 
# #  the smaller of two even number  but  return greater one if one of them
# #  is odd 

# #  here  the  some  alternative  we cam do to my first code 

# # sol2
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         return min(a, b)
#     else:
#         return max(a, b)

# a = int(input("Enter the even number a: "))    
# b = int(input("Enter the even number b: "))  
# print(lesser_of_two_evens(a, b))


# # QUESTION 2:>ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

# sol
# def animan_cracker(str):
#     word=str.split()
#     if(word[0][0]==word[1][0]):
#         return True
    
#     else:
#         return False
    
# str_=input("Enter the string containing two Word")
# print(animan_cracker(str_))



# # Question 3:MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

# # sol
# def makes_twenty(a,b):
#     if(a+b==20):
#         return True
    
#     elif (a == 20 and b != 20) or (b == 20 and a != 20):
#         return True

    
#     else:
#         return False
    
# a=int(input("Enter the number a:"))
# b=int(input("Enter the number b:"))
# print(makes_twenty(a,b))

# LEVEL 1 
# QUESTION1:>OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# # sol:
# def old_macdonald(str):
#     newstr=""
#     for i in range(len(str)):
#         newstr=str[0].capitalize()+str[1:3]+str[3].capitalize()+str[4:]
     
#     return newstr

# str_=input("Enter the string:")
# print(old_macdonald(str_))

# # Question 2 :>MASTER YODA: Given a sentence, return a sentence with the words reversed

# # sol:>
# def master_yoda(str):
#     word=str.split()
#     word_=word[::-1]
#     newstr_=" ".join(word_)

#     return newstr_

# print(master_yoda("I am home"))

# QUESTION 3:> ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200'

# # sol
# def almost_there(n):
#     return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

# print(almost_there(90)) 

# Question 4:>FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# def has_33(list):
#     for i in range(len(list) - 1):
#         if(list[i]==3 and list[i+1]==3):
#             return True
#     return False

# nums=[]
# n=int(input("enter the number of item you want in list"))
# for i in range(n):
#     el=int(input("Enter the element of the list"))
#     nums.append(el)

# print(nums)
# print(has_33(nums))


# QUESTIOn4:>PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

# sol 
# def paper_doll(str):
#     result=""
#     for  i in str:
#         result+=i*3
#     return result

# str_=input("enter The string:")   
# print(paper_doll(str_))

# QUESTION :> BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# sol

# def blackjack(a,b,c):
#     if(a+b+c<=21):
#         return a+b+c
#     elif(a+b+c>21 and (a==11 or b==11 or c==11)):
#         return (a+b+c)-10
    
#     else:
#         return 'BUST'
    
# print(blackjack(9,9,11))

# QUESTION:>SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

# sol:
# def summer_of_69(arr):
#     total = 0
#     skip = False  # Flag to skip numbers between 6 and 9

#     for num in arr:
#         if num == 6:
#             skip = True
#         elif num == 9:
#             skip = False
#         elif not skip:
#             total += num

#     return total

# print(summer_of_69([2,1,6,9,11]))

# CHALEENGING PROBLEMS

#QUESTION:>SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

# # sol:
# def spy_game(nums):
    
#     zero_count = 0
    
#     for num in nums:
#         if num == 0:
#             zero_count += 1
#         elif num == 7 and zero_count >= 2:
#             return True
    
#     return False

# print(spy_game([1,7,2,0,4,5,0]))
# important
# print("Program to  check number of prime number upto  the  given numbers")
# import math

# def is_prime(num):
#     # Prime numbers are greater than 1 they are not  less than 1
#     if num <= 1:
#         return False

#     # Check for divisibility from 2 to the square root of num
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False

#     return True

# def count_primes(n):
#     count = 0
#     for num in range(2, n + 1):
#         if is_prime(num):
#             count += 1
#     return count

# n=int(input("Enter the number :"))
# print(count_primes(n))


# def has_33(list_):
#     for num in list_:
#         if(num==3 or num+1==3):
#             return True
      
#     return False

# li=[]
# n=int(input("Enter the number"))
# for i in range(n):
#     el=int(input(f"Enter the element:{i+1}\n"))
#     li.append(el)
# print(has_33(li))


# def paper_doll(str):
#     re=""
#     for c in str:
#        re+=c*3
#     return re
    

# print(paper_doll("hello"))

# def blackjack(a,b,c):
#     if(a+b+c<=21):
#         return a+b+c
#     elif(a+b+c>21 and (a==11 or b==11 or c==11)):
#         return (a+b+c)-10
    
#     else:
#         return 'BUST'
    
# print(blackjack(9,9,9))
         
# def summer_69(list):
#     total=0
#     skip=False

#     for num in list:
#         if num==6:
#             skip=True
#         elif num==9:
#             skip==False

#         else:
#             total+=num

#     return total
# print(summer_69([1,3,5]))



# def spy_game(nums):
    
#     zero_count = 0
    
#     for num in nums:
#         if num == 0:
#             zero_count += 1
#         elif num == 7 and zero_count >= 2:
#             return True
    
#     return False

# print(spy_game([1,2,1,0,7,5]))

# import math
# def is_prime(num):
    
#     if num <= 1:
#         return False

    
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False

#     return True

# def count_primes(n):
#     count = 0
#     for num in range(2, n + 1):
#         if is_prime(num):
#             count += 1
#     return count

        
# print(count_primes(100))
    
    
# def square(nums):
#     return nums**2

# lis=[1,5,6,8,10]
# lis_=[]
# for num in lis:
#     s=square(num)
#     lis_.append(s)

# print(lis_)

# for item in map(square,lis):
#     print(item)

# def splicer(str):
#     if(len(str)%2==0):
#         return 'EVEN'
#     else:
#         return str[0]
# nam=["hello","jenny","anchal"]
# for num in filter(splicer,nam):
    
#     print(num)
    
# print(list(map(splicer,nam)))

# square=lambda x:x**2
# print(square(5))

# import math
# def vol(rad):
#     return 4/3*3.14*(math.pow(rad,3))

# print(vol(2))

# def up_low(s):
#     uppercount = 0
#     lowercount = 0
#     symb_spa_special = 0

#     for i in s:
#         if i.isupper():
#             uppercount += 1
#         elif i.islower():
#             lowercount += 1
#         else:
#             symb_spa_special += 1

#     print("The number of uppercase characters is:", uppercount)
#     print("The number of lowercase characters is:", lowercount)
#     print("The number of symbol/special character/space characters is:", symb_spa_special)

# s_ = input("Enter the string or sentence: ")
# up_low(s_)


# this  is the code to remove the  repititive term or number in the list

# def unique_list(list):
    
#     un=[]
#     for i in list:
#         if i not in un:
#             un.append(i)
#     return un
    
# list_=[1,2,2,3,4,4,5,5,5,6]
# print(unique_list(list_))


# def unique_lis1(lst):
#     return list(set(lst))

# print(unique_lis1(list_))

# def multi(lst):
#     mult=1
#     for i in lst:
#         mult*=i
#     return mult
    

# li=[1,2,8,6,3,9]
# print(multi(li))


# def pallindrome(s):
#     if(s[::-1]==s):
#         print("pallindrome")

#     else:
#         print("nope !! no palindrome")

# s_=input("Enter the string:")
# print(pallindrome(s_))

# pangram

# def is_pangram(s):
#     uni=set()

#     for char in s:
#         if 'a' <=char>='z':
#             uni.add(char)
    
#     return len(uni)==26

# s="The quick brown fox jumps over the lazy dog"

# if is_pangram(s.lower()):
#     print("The string is a pangram")
# else:
#     print("The is not a panrgam")