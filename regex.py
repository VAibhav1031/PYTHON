import re
# Comment out  step  by step to check

# Character	Description	Example	Try it
# []	A set of characters	"[a-m]"	
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"planet$"	
# *	Zero or more occurrences	"he.*o"	
# +	One or more occurrences	"he.+o"	
# ?	Zero or one occurrences	"he.?o"	
# {}	Exactly the specified number of occurrences	"he.{2}o"	
# |	Either or	"falls|stays"	
# ()	Capture and group


# str1="/*Jon is @developer & musician"
# sd=re.sub(r'[^\w\s]','',str1)

# print(sd)


# str="the  water is 444-555-6666  455-885-862  goonns"

# d=re.search("\d{3}-\d{3}-\d{3}",str)
# d=re.findall("[^a-zA-Z\s]",str)
# d=re.findall(r"[^\w\s]",str)
# print(d)


# txt="The rain in Spain"
# x=re.findall("ai",txt)
# x=re.search("\s",txt)
# x=re.split("\s",txt,2)
# print(x)


# str="Hey there is anyone56 2 _ caleed"
# x=re.findall("\w",str)
# print(x)

# def is_allowed_char(str):
#     char=re.compile(r'[\w]')
#     str=char.search(str)
#     return bool(str)

# print(is_allowed_char("ABCDEFGabcdefg123450"))
# print(is_allowed_char("@#$%^&"))


# # followed  by zero or more occurence

# def match(str):
#     pattern="^a(b*)$"
#     if re.search(pattern,str):
#         return "Found a match"
#     else:
#         return "Not a match"
# print(match("ac"))
# print(match("ab"))
# print(match("acb"))
# print(match("abb"))

# print()

# # followed by the 1 or more occurence
# def match(str):
#     pattern="^a(b+)$"
#     if re.search(pattern,str):
#         return "Found a match"
#     else:
#         return "Not a match"
# print(match("ac"))
# print(match("ab"))
# print(match("acb"))
# print(match("abb"))


# print()

# # followed by xero or one  occurence
# def match(str):
#     pattern="^a(b?)$"
#     if re.search(pattern,str):
#         return "Found a match"
#     else:
#         return "Not a match"
# print(match("ac"))
# print(match("ab"))
# print(match("acb"))
# print(match("abb"))


# print()

# # string that has an a followed by two to three 'b'.
# def match(str):
#     pattern="a(b{2,3})" #"^a(b{2,3}$)" if we use this then a 
#                         # patricular string have to be their nota sentence
#     if re.search(pattern,str):
#         return "Found a match"
#     else:
#         return "Not a match"
# print(match(" hey ther abbcc"))  # Truee by removing ^ $ for particular string
# print(match("abbb"))
# print(match("abb"))

# # find sequences of lowercase letters joined by an underscore.

# def match(str):
#     pattern="[a-z]+_+[a-z]+"
#     z=re.search(pattern,str) # to  search another one also we can use
#                              #findall function to search other 
#     if z:
#         return z  #use z.group()  to get the  actual search result
#     else:
#         return "Not matched"
    

# print(match("hey ther cbd_kol mis_uo are goinf up"))


# # Let's find all search pattern


# def match(str):
#     pattern="[a-z]+_+[a-z]+"
#     z=re.findall(pattern,str)
#     if z:
#         return z  
#     else:
#         return "Not matched"
    

# print(match("hey ther cbd_kol mis_uo are goinf  like  thumbs_up up"))




# Write a Python program to find the sequences of one 
# upper case letter followed by lower case letters.


# def match(str):
#     pattern="[A-Z]+[a-z]+"
#     res=re.findall(pattern,str)
#     if res:
#         return "found a match",res
    
#     else:
#         return "Not matched"
    

# print(match("The person is Gonna"))

# for particular word
# def match(str):
#     pattern="[A-Z]+[a-z]+$"
#     res=re.findall(pattern,str)
#     if res:
#         return "found a match",res
    
#     else:
#         return "Not matched"
    

# print(match("TheGonna"))
# print(match("AaBcGg"))


# # matches a string that has an 'a' followed by anything ending in 'b'.
# def match(str):
#     pattern="a.*b$"   #  here  you can  think . as inputs come between
#                       # for  example hello-"he..o"-> pattern  
#                       # and *-> for occurence symbol (0 or more )
#                       # because we want a start and end with b  dont know how much in between
#     res=re.search(pattern,str)
#     if res:
#         return res
#     else:
#         return "Not matched"
    
# print(match("when  the alveb"))


# program that matches a word at the beginning of a string.
# def match(str):
#     pattern="\Ahey"
#     res=re.search(pattern,str)

#     if res:
#         return res
#     else:
#         return "Not matched"
    
# print(match("hey there"))

# print()

# def match(str):
#     pattern="^\w+"
#     res=re.search(pattern,str)

#     if res:
#         return res
#     else:
#         return "Not matched"
    
# print(match("hey there"))


# ***********************************************

# Write  a program in python that matches a word containing the z
# def match(str):
#     pattern="\w*z\w*"

#     res=re.search(pattern,str)
#     if res:
#         return "Found a match",res.group()
    
#     else:
#         return "Not match"
    
# print(match("the quick brown fox jumps over the lazy dog"))
# print(match("bhjsds there iyou  must  lshdk"))


# *****************************************
# we  have  to check for  one  string  so for that  we have to 
# ^ $
# def mx(str):
#     pattern="^[a-zA-Z0-9_]*$"
#     rs=re.search(pattern,str)
#     if rs:
#         return "Matched"
#     else:
#         return "Not matched"
    
# print(mx("The quick brown fox jumps over the lazy dog."))
# print(mx("Python_exerex_1"))


# A  string   start with specified number or not 
# def mx(str):
#     pattern="^[0-9]"   # for  specified given number we can ^5
#     rs=re.search(pattern,str)
#     if rs:
#         return "Matched"
#     else:
#         return "Not matched"
    
# print(mx("The quick brown fox jumps over the lazy dog."))
# print(mx("1-7825hey"))


# To remove the leading zeros  from the ip addres
# def rem_zer(str):
#     pattern="0*"
#     res=re.sub(pattern,"",str)
#     return res

# ip = "216.08.094.196"
# print(rem_zer(ip))
    

# # Check the number at the end of the  string
# def chk(str):
#     pt="\w*[0-9]$"
#     res=re.search(pt,str)
#     if res:
#         return "Matched ",res.group()
#     else:
#         return "Not matched"
    
# print(chk("hey theat how cloud9"))

# dont mind i just  converted the   string list containig number as str
# to integer
# def matched(str):
#     pat="\d{1,3}"
#     res=re.findall(pat,str)
#     s=list(map(int,filter(lambda x: x.isdigit(),res)))
    
#     if res:
#         return s
    
#     else:
#         return "Not matched"
    
# print(matched("Exercises number 1, 12, 13, and 345 are important"))


# *********************************************

# write a python program  to  search  for  literal strings  within a string

# patterns=["fox","dog","horse"]
# test="The quick brown fox jumps over the lazy dog"

# for x in patterns:
#     print("Searching for the %s  in %s" % (x,test),)
#     if re.search(x,test):
#         print("Matched ")

#     else:
#         print("Not matched")



# Write a Python program to search for a literal string in a string and also find the 
# location within the original string where the pattern occurs.

# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'


# patterns=["fox"]
# test="The quick brown fox jumps over the lazy dog"

# for x in patterns:
#     print("Searching for the %s  in %s" % (x,test),)
#     s=re.search(x,test)
#     if re.search(x,test):
#         print("Matched and location is-> ",s.span())

#     else:
#         print("Not matched")




# l=[1,2,65,50]
# l1=[2,5,6,8]
# print(l1+l)

# import numpy as np
# a=np.array([[1,2,3,4,14,2,5,4,45]])
# m=np.reshape(a,(3,-1))
# print(m)


# s="Python exercises,PHP exercises, C# exercises"
# pattern="exercises"
# s=re.findall(pattern,s)
# print(s)

# for match in s:
#     print("found %s" % match)


# for match in re.finditer(pattern,s):
#     s_=match.start()
#     e=match.end()
#     print("Found %s at %d:%d" % (s[s_:e],s_,e))




# Write a python progrram to replace  whitespaces with an underscore and 
# vice versa
# Solution:

# text="hey ther are something you wantr   to know  please tell me where are you "

# pattern="\s"

# ch=input("Underscore(_) or White space (/s)")
# if ch=="_":
#     rs=re.sub(pattern,"_",text)
# if ch=="/s":
#     rs=re.sub(pattern,pattern,text)
# print(rs)

# # to  find the day date and monthe  from the  url
# sample_url="https://www.nytimes.com/2024/03/07/world/europe/ukraine-war-latest.html"
# year="(\d{4})/(\d{2})/(\d{2})"
# f=re.search(year,sample_url)

# if f:
#     year=f.group(1)
#     month=f.group(2)
#     day=f.group(3)
#     print("Year:",year)
#     print("month:",month)
#     print("day:",day)

# else:
#     print("There is no date  day and month in it ")


# Write  a python program  to convert  adate of  yyyy-mm-dd format to  dd-mm-yyyy format

# tet="An archaeological dig scheduled for 2023-12-15 in the Giza plateau has sparked excitement among historians. The dig aims to uncover potential hidden chambers or secret passages near the Great Pyramid of Giza. Meanwhile, on 2024-02-14, the world celebrated Valentine's Day, a day dedicated to love and affection. While the origins of this holiday remain debated, its traditions of exchanging cards, flowers, and chocolates have become a global phenomenon. These events, separated by just a few months, highlight the diverse interests and experiences that capture our attention throughout the year."

# pattern="(\d{4})-(\d{2})-(\d{2})"
# fd=re.sub(pattern,r"\3-\2-\1",tet)

# print(fd)

# # Search for the  words statring with  P letter in a words  of  list
# words = ["Python PHP", "Java JavaScript", "c c++"]

# for w in words:
#     sd=re.match("(P\w+)\W(P\w+)",w)

#     if sd:
#         print(sd.groups())

# # Abbreviating the Road as Rd
# wi="hey which  Road are you takinf for this  trip and  which Road for home"
# rs=re.sub("Road","Rd",wi)
# print(rs)

# # Write a Python program to find all words starting with 'a' or 'e' in a given string.
# text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

# pattern="[ae]\w+"

# rd=re.findall(pattern,text)
# print(rd)

# while  using the  split  functio giving the  parameter we  are 
# get the result   having that  condition  removed  in the list form

# # Write a Python program to separate and print the numbers in a given string.
# text="Ten 10, Twenty 20, Thirty 30"
# result=re.split("\D+",text)
# print(result)


# for element in result:
#     print(element)

# # Write  a program  to  replace all ocurrence  of a space,comma,or dot with a colon


# sd="Python Exercises, PHP exercises."
# pattern="[\s,.]"
# dk=re.sub(pattern,":",sd,2)
# print(dk)

# #  Write a Python program to find all five-character words in a string.
# text='The quick brown fox jumps over the lazy dog.'
# pattern="\w{5}"
# es=re.findall(pattern,text)
# print(es)

# #  Write a Python program to find all words that are at least 4 characters long in a string.

# # solution: 
# text='The quick brown fox jumps over the lazy dog.'
# pattern="\w{4,}",te
# rs=re.findall(pattern,text)
# print(rs)




# # Write a Python program to find all three, four, and five character words in a string.
# # Solution
# text='The quick brown fox jumps over the lazy dog.'
# pattern="\w{3,5}"
# rs=re.findall(pattern,text)
# print(rs)

# # Write a Python program to convert a camel-case string to a snake-case string.
# def camel_to_snake(text):
#     str=re.sub('(.)([A-Z][a-z]+)',r'\1_\2',text)
#     return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str).lower()

# print(camel_to_snake("My_Name"))



# import re

# def camel_to_snake(camel_case_string):
#     pattern = re.compile(r'(?<!^)(?=[A-Z])')
#     # Replace camel case with underscores
#     snake_case_string = re.sub(pattern, '_', camel_case_string).lower()
#     return snake_case_string

# # Example usage:
# camel_string = "CamelCaseString"
# snake_string = camel_to_snake(camel_string)
# print(snake_string) 


# Write a Python program to extract values between quotation marks of a string.
def ex_val_quotation(text):
    pattern="'(.*?)'"  #'(.?*)'  .->any character except new line    ?* greddy  character(can zero / or more ocurrence) 
    df=re.findall(pattern,text)

    return df
print(ex_val_quotation("The persion  is 'here' 'Asus' "))



