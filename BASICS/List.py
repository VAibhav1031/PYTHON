# ***************************************************************
# List  :

#Here WAPP ->Write A Python Program 



# # WAPP  to  sum all  the  elements in a list.
# # 1 way
# def cu(lis):
#     return sum(lis)

# print(cu([10,2,13,8,5]))

# # 2 way

# def sum_list(list):
#     sum_=0
#     for x in list:
#         sum_+=x

#     return sum_

# print(sum_list([10,2,13,8,5]))



# # WAPP python program to Multiply all the items in a list .

# def mul_ele(list):
#     t=1
#     for x in list:
#         t*=x

#     return t

# print(mul_ele([2,5,8,10,12]))




# # WAPP to get the  largest number from a list
# # 1 way
# def max_ele(list):
#     return max(list)

# print(max_ele([10,10.81,10.8105,10.89,10.888,10.79]))

# # 2 way
# def max_el(list):
#     max=list[0]
#     for x in list:
#         if x>max:
#             max=x

#     return max
# print(max_el([10,10.81,10.8105,10.89,10.888,10.79]))




# # WAPP to get the  smallest number from a list
# # 1 way
# def min_ele(list):
#     return min(list)

# print(min_ele([10,10.81,10.8105,10.89,10.888,10.79]))

# # 2 way
# def min_el(list):
#     min=list[0]
#     for x in list:
#         if x<min:
#             min=x

#     return min
# print(min_el([10,10.81,10.8105,10.89,10.888,10.79]))




# # WAPP to count  the number of  strings  from a given  list of  strings.The string length


# def  match_words(words):
#     count=0

#     for word in words:
#         if len(word)>1 and word[0] == word[-1]:
#             count+=1


#     return count

# print(match_words(['abc', 'xyz', 'aba', '1221']))



# #  Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# # Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# def sort_by_last_element(list):
#     return sorted(list,key=lambda x:x[-1])

# print(sort_by_last_element([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# # WAPP to remove duplicates from a list
# def remove_dupl(lis):
#     return list(set(lis))

# print(remove_dupl([1,2,3,5,5,4,5,6,8]))

# # WAPP to check if a list is empty or not

# def check_emp(lis):
#     if len(lis)==0:
#         return "empty"
#     else:
#         return "Not Empty"
    
# print(check_emp([]))


# def check_list(str,n):
#     txt=str.split(" ")
#     word_len=[]

#     for s in txt:
#         if len(s)>n:
#             word_len.append(s)
#     return word_len
# print(check_list("The quick brown fox jumps over the lazy dog",4))


# # WAPP to generate 3*4*6 3D array whose each element is *.

# arr=[[['*' for col in range(6)]  for col in range(4)]  for row in range(3)]
# print(arr)


# # WAPP to print the numbers of a specified list after  removing even  numbers from it

# def el(lis):
#     return[x for x in lis if x%2!=0]

# print(el([1,2,3,8,6,5,13]))


# # WAPP to shuffle and  print a  specified list
# import random
# def shuff(lis):
#     random.shuffle(lis)
#     return lis
# print(shuff([1,2,3,4,5]))
 


# # WAPP to  generate and print a lisr of  the  first and last  5 elemenrs where the values are square numbers


# def listu():
#     l=[]
#     for  i in range(1,21):
#         l.append(i**2)

#     print(l[:5])
#     print(l[:-5])

# listu()




# # WAPP  to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# # Sample Data:
# # ([0, 3, 4, 7, 9]) -> False
# # ([3, 5, 7, 13]) -> True
# # ([1, 5, 3]) -> False


# # To  write the  main program  let's  do it  with  some  basic  concept  of the  prime

# import math

# def check_prime(n):

#     if n<1:
#         print("Prime number cannot be less than 1") # optional  you can  do this
#         return False
#     else:
#         for i in range(2,math.isqrt(n)+1):
#             if n%i==0:
#                 return False
        
#         return True
    
# # print(check_prime(32))

# def print_prime(start,end):
#     for i in range(start,end+1):
#         if check_prime(i):
#             print(i)

      

# # print_prime(5,12)

                     
# # Now check  prime will use thing  in   list  of elements   whethere they are primenumber
         
# def check(list):
#     for x in list:
#         if check_prime(x):
#             return True
#         else:
#             return False

# print(check([0,3,4,7,9]))
  



# # WAPP to generate all permutation of a list in python
# import itertools

# print(list(itertools.permutations([1,2,3,4])))


# # WAPP  to calculate  the  difference between the  two  list

# def cal_diff(list1,list2):
#     dlis1=list(set(list1)-set(list2))
#     dlis2=list(set(list2)-set(list1))

#     total_lis=dlis1+dlis2
#     print(total_lis)

# cal_diff([1,3,5,7,9],[1,2,4,6,7,8])


# # WAPP to access the index of the  list

# l=[2,8,9,10,12,42]
# print(l.index(2))

# for num_index,num_val in enumerate(l):
#     print(num_index,num_val)


# # WAPP to convert the characters  of the  list to string
# # ['s','t','r','i','n','g','s'] --> "strings"

# # 1 way
# def con(list):
#     s=""
#     for x in list:
#         s+=x

#     return s

# print(con(['s','t','r','i','n','g','s']))

# # 2 way

# # is to use the  join method

# l=['s','t','r','i','n','g','s']
# s=''.join(l)
# print(s)


# # WAPP to find the second smallest number in a list

# def second_smalles_ele(lst):
#     if len(lst) < 2:
#         print("List has less than 2 elements.")
#         return lst[0]
    
#     m = max(lst)
#     n = list(set(lst) - set([m]))

#     if not n:  # If n is empty, it means all elements in the list are the same
#         print("All elements in the list are the same.")
#     else:
#         smal = max(n)
#         print("First smallest element:", m)
#         print("Second smallest element:", smal)

# second_smalles_ele([2,2.5,2.01,1.99,1.9905,1.98999])
# second_smalles_ele([1, 2, -8, -2, 0, -2])


# # WAPP to find the second largest number in  the list
# def second_largest_ele(lst):
#     if len(lst) < 2:
#         print("List has less than 2 elements.")
#         return lst[0]

#     m = max(lst)
#     n = list(set(lst) - set([m]))
    
#     if not n:  # If n is empty, it means all elements in the list are the same
#         print("All elements in the list are the same.")
#     else:
#         smal = max(n)
#         print("First Largest element:", m)
#         print("Second Largest element:", smal)

# # Test cases
# second_largest_ele([1, 1, 1, 0, 0, 0, 2, -2, -2]) 
# second_largest_ele([1, 1]) 
# second_largest_ele([5]) 



# # WAPP to check whether two lists are circularly identical

# def are_circularly_identical(lst1,lst2):
#     if len(lst1)!=len(lst2):
#         return False
    
#     extended_lst1=lst1+lst1

#     if lst2 in [extended_lst1[i:i+len(lst2)] for i in range(len(lst1))]:
#             return True
    
#     else:
#          return False
    

# print(are_circularly_identical([1,2,3,4,5],[3,4,5,1,2]))
# print(are_circularly_identical([1,2,3,4,5],[5,4,3,2,1]))




# # WAPP to get the frequency of elements in a list

# def freq_list(lis):
#     count=0
#     for i in   range(len(lis)):
#         count+=1

#     return count

# print(freq_list([2,5,8,6,10]))


# # WAPP to  get the count   of elements  on specified range in list

# def freq_spec_lis(lis,start,end):
    
#     count=0
#     for i in lis:
#         if start<=i<=end:
#             count+=1


#     return  count



# print(freq_spec_lis([2,5,10,31,5,10,5,8,14],10,14))



# # WAPP to check whethere a list contains a sublist
# import itertools
# def check_sub(sub,lis):
#     for n in sub:
#         if n not in lis:
#             return False
        
#         return True

    
# print(check_sub([7,9,8],[2,5,6,7,8,9,10]))


# # WAPP  to generate the  sublists from  a list

# def sublist(list):
#     sb=[]
#     n=len(list)
#     for i in range(1,n+1):
#         for s in range(n-i+1):
#             sb.append(list[s:s+i])
#     return sb
# print(sublist([1,2,3,5,6]))


# def concat_list(lis,n):
#     return ['{}{}'.format(x,y) for y in range(1,n+1) for x in lis]
    
# print(concat_list(['p','q'],5))


# # WAPP to find the common items in two lists
# # 1way
# def common_ele(list1,list2):
#     common=[]
#     for i in list1:
#         for j in list2:
#             if i==j:
#                 common.append(i)
#     return common

# print(common_ele(["Red","Balack","Orange","pink"],["Red","Green","Orange","White"]))


# # 2Way

# color1=("Red","Green","Orange","White")
# color2=("Black","Green","White","Pink")
# print(set(color1)& set(color2))


# # WAPP  to get  a variable with an identification number or string.
# x=100
# print(id(x))
# print(format(id(x),'x'))

# s='w3resource'
# print(format(id(s),'x'))


# # WAPP  to convert  a list of multiple integers into a single  integer
# # 1 way
# def mul(list):
#     l=""
#     for i in list:
#         l+=str(i)
#     s=int(l)
#     # print(type(s))
#     return s

# print(mul([12,35,46]))

# #  2way 

# l=[12,35,46]
# print("Original List: ",l)

# x=int("".join(map(str,l)))

# print("Single integer: ",x)


# # WAPP  to  change the  position of every n-th value to the  (n+1)th in a list

# def pos(list):
#     for i in range(len(list)-1):
#        temp=list[i]
#        list[i]=list[i-1]
#        list[i-1]=temp



#     return list

# print(pos([2,5,8,9]))


# WAPP to  create  a multiple list

# # 1 way
# num=5

# lis=[[] for x in range(num)] # Easiest  way to cre
# print(lis)

# # 2 way
# num_range=10
# nlis=[]
# for i in range(num_range):
#     li=[]
#     nlis.append(li)
# print(nlis)


# # WAPP  to find the  missing and  additional values in two lists

# def miss_add_val(list1,list2):
#     add_val1=[]
#     miss_val1=[]
#     add_val2=[]
#     miss_val2=[]
#     for i in list1:
#         if i  not in list2:
#             add_val1+=i
#             miss_val2+=i
#     for i in list2:
#         if i not in list1:
#             add_val2+=i
#             miss_val1+=i
#     print()
#     print("List 1 :",list1)
#     print("List 2 :",list2)
#     print()
#     print("On comparing list1 with list2")
#     print("Missing Value in list1 :  ",miss_val1)
#     print("Additional value  in list2 :",add_val1)
#     print()
#     print("On comparing list2 with list1")
#     print("Missing Value in list 2 :  ",miss_val2)
#     print("Additional value in list 2 :",add_val2)


# miss_add_val(['a','b','c','d','e','f'],['d','e','f','g','h'])


# # WAPP to split  a list into a variables
# color=[
#     ("Black","#00000","rgb(0,0,0)"),
#     ("Red","#FF000","rgb(255,0,0)"),
#     ("Yellow","FFFF00","rgb(255,255,0)")
# ]


# var1,var2,var3=color

# print(var1)
# print(var2)
# print(var3)


# # WAPP to  genetrat the group of consecutive number in the list
# l=[[5*i+j for j in range(1,6)] for i in range(5)]
# print(l)



# # WAPP to convert a pair of  values into  a sorted unique array

# # list of  pair-values(tuples)
# l=[(1,2),(3,4),(1,2),(5,6),(7,8),(1,2),(3,4),(3,4),(7,8),(9,10)]
# ll=[]

# for i in l:
#     for j in i:
#         ll.append(j)

# s=sorted(list(set(ll)))
# print(s)


# # k = [j for i in l for j in i]
# # print(k)


# # WAPP to insert an element before each element of a list.

# # # Let's take the list
# # l=[2,5,6,8,10]

# # for i in range(len(l)-1):
# #     b=int(input("Enter :"))
# #     l.insert(i,b)
# # print(l)


# l=[2,5,6,8,10]
# n_l=[]
# for item in l:
#     b=int(input(f"Enter element to insert before {item} : "))

#     n_l.append(b)
#     n_l.append(item)

# print(n_l)


# # WAPP to print nested lists (each list on a new line) using the print() function.
# # 1 way
# # n=[[2,5,5],[3,5,6]]
# # for i in n:
# #     print(i)
    
# # 2 way
# #print('\n'.join([str(k) for k in n]))


# # WAPP to convert a list to a list of dictionaries.
# # Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# # Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

# # 

# l= ["Black", "Red", "Maroon", "Yellow"]
# l2=["#000000", "#FF0000", "#800000", "#FFFF00"]
# d1={}

# color_co=[]


# # We just use the  zip  function  which  helps to group them 
# # and  can access them  with  two keyword  first  for first lis
# # and second for second list

# for color_name,color_code in zip(l,l2):
#     d1["color name"]=color_name
#     d1["color code"]=color_code

#     color_co.append(d1)

# print(color_co)



# # WAPP  to sort a list of nested dictionaries.

# my_list=[{'key':{"subkey":1}},{'key':{'subkey':10}},{'key':{'subkey':5}}]
# print("Original list")
# print(my_list)
# my_list.sort(key=lambda e: e['key']['subkey'], reverse=True) # in reverse or  descending order
# print("sorted list")
# print(my_list)


# # WAPP to split  a list every Nth element

# s_l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# def split(list,n):
#     return [list[i::n] for i in range(n)]


# print(split(s_l,3))


# # WAPP to compute the  difference between two lists
# # Sample data : ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]

# # Expected Output:
# # Color1-Color2: ['white', 'orange', 'red']
# # Color2-Color1: ['black', 'yellow']

# # Solution


# color1=["red", "orange", "green", "blue", "white"]

# color2=["black", "yellow", "green", "blue"]

# print("Color1-Color2",list(set(color1)-set(color2)))
# print("Color2-Color1",list(set(color2)-set(color1)))


# s_l=[1,3,5,7,9,10]
# l=[2,4,6,8]
# s_l[-1:]=l
# print(s_l)


# # WAPP to concatenate elements of a list
# # Sample-> ['red','green','orange']
# # output 1-> [redgreenorange]
# # output 2-> [red-green-orange]

# def conca(list):
#     s=""
#     l=[]
#     for i in range(len(list)):
#         s+=list[i]
#     l.append(s)
#     return l
# print(conca(["Red","Green","orange"]))



# def conc(lst):
#     return  ''.join(lst)
# print(conca(['Red','Green','orange']))


# # WAPP to remove key-value pairs from a list of  dictionaries

# def convert(lis):
#     l=input("Enter the key")
#     return [{k:v for k,v in i.items() if k!=l} for i in lis]

# original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]

# print(convert(original_list))


# def desconvert(lis):
#     l=int(input("Enter the key : "))
#     for d in lis:
#         d.pop(l)
#     return lis

# print(convert(original_list))



# # WAPP to convert a string  to  a list:

# # Basic 
# st="heree we are let's  go"
# l=st.split()
# print(l)

# l1=list(st) # this  will make  the thing  one letter by and it also count white space in it
# print(l1)


# # WAPP to  check if all items in a given list of strings are equal to a given string.

# # Eaay peasy

# string="Blue"
# dic={"green","orange","black","white"}
# if string in dic:
#     print("True")
# else:
#     print("False")

# # all
# # all() function is a built-in function that returns True if all elements in an iterable are true, otherwise it returns False. 
# # It takes an iterable(such as a list, tuple, or set) as its argument and evaluates each element in the iterable in a boolean context
# dic={"green","orange","black","white"}
# print(all(co=="Blue" for co in dic))

# #  example

# numbers=[1,2,3,4,5,6]
# print(all(num>0 for num in numbers)) # returns True

# numbers=[2,4,6,7,10] # every  element must be true then only ot  will be return  true
# print(all(num%2==0 for num in numbers)) # returns False

# numbers=[2,4,6,8,10]
# print(all(num%2==0 for num in numbers)) # returns True  all is true




# # Again Easy peasy
# # WAPP to count integers in a given mixed list.

# def count_int(li):
#     count=0
#     for i in li:
#         if isinstance(i,int):
#             count+=1
#     return count

# print(count_int([1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]))
        

# # WAPP to remove  a specified column from a given nested list.

# l=[[1,2,3],[2,4,5],[1,1,1]]
# l1=[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# def rem_sp(l):
#     return[l[i][1:] for i in range(len(l))]

# print(rem_sp(l))
# print(rem_sp(l1))



# # WAPP to  rotate a given list by a specified number of items in the right or left direction.

# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def right_(lis,n):
#     return lis[n-1:]+lis[:n]

# def left_(lis,n):
#     return lis[n:]+lis[:n]


# print(right_(l,4))
# print(left_(l,2))

# # this is the  function i create  to  get the result  but you  can  change it 
# # according to  your  need



# # WAPP to find the item with most ocurrences in a given list.
# # Original list:
# # [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# # Item with maximum occurrences of the said list:
# # 2


# from collections import Counter

# def most_common_element(lst):
#     counter = Counter(lst) # Make the dictionry of the(list,tuple) to whick  key are elements(of tuple,list) and  value are the number of occurence
#     most_common = counter.most_common(1) # this  return the  list having element as a tuple
#     print(most_common) # here  by this  you will see that  it  have  that dict thing in tuple  form
#     return most_common[0][0] if most_common else None

# # Example usage:
# my_list=[5,6,8,2,8,2,6,2,3,5,2,2]
# result = most_common_element(my_list)
# print("Most common element:", result)


# # WAPP to acess multiple elements at a specified index from a given list

# org_li=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

# def list_index(lis,index_lis):
#     return[lis[i] for i in index_lis]


# list_in=[0,3,5,7,10]
# print(list_index(org_li,list_in))

# # WAPP to extract the nth element from a given list of tuples.
# # Original list:
# # [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# # Extract nth element ( n = 0 ) from the said list of tuples:
# # ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
# # Extract nth element ( n = 2 ) from the said list of tuples:
# # [99, 96, 94, 98]



# l=[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]

# def re_nth(lis,n):
#     if(n==0):
#         return[d[0] for d in lis]
#     elif(n==1):
#         return[d[1] for d in lis]
#     else:
#         return[d[n] for d in lis]
    

# print(re_nth(l,2))
    


# WAPP that takes a list of integers and finds all pairs of integers that differ by three. Return all pairs of integers in a list.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> [[0, 3], [4, 7]]
# [0, -3, -5, -7, -8] -> [[-3, 0], [-8, -5]]
# ([1, 2, 3, 4, 5]) -> [[1, 4], [2, 5]]
# ([100, 102, 103, 114, 115]) -> [[100, 103]]

# def find_pairs_differ_by_three(lst):
#     pairs = []
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if abs(lst[i] - lst[j]) == 3:
#                 pairs.append([lst[i], lst[j]])
#     return pairs

# # Sample Data
# sample_data = [
#     [0, 3, 4, 7, 9],
#     [0, -3, -5, -7, -8],
#     [1, 2, 3, 4, 5],
#     [100, 102, 103, 114, 115]
# ]

# # Test the function with sample data
# for i, data in enumerate(sample_data, start=1):
#     print(f"{i}. {data} -> {find_pairs_differ_by_three(data)}")



# # WAPP  extract the first specified number of vowels from a given string. If the specified number is less than the number of vowels present in the string then display "n is less than the number of vowels present in the string".
# # Sample Data:
# # ("Python", 2) -> "n is less than number of vowels present in the string."
# # ("Python Exercises", 3) -> "oEe"
# # ("aeiou") -> "AEI"



# def  numb_vowels(lis,n):
#     re=""

#     for  i in lis:
#         if i  in "aeiouAEIOU":
#             re+=i

#     return re[:n] if(len(re))>=n   else "n is less than specified vowels"


# print(numb_vowels("python",2))
# print(numb_vowels("Python Exercises",3))



# # WAPP to creating  a new  list  by dividing the  two  list ele 


# def new_2(list1,list2):
#     if (len(list1)==len(list2)):
#         s=[x/y for x,y in zip(list1,list2)]
#         return s
#     else:
#         return "Number of elements are not equal in the Lists" 

# print(new_2([2,5,8,6,9],[2,3,5,7,9,2]))



# # WAPP  to find common elements in a given list of lists.
# # Original list:
# # [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]
# # Common elements of the said list of lists:
# # [2, 3]

# def commo(lis):
    
#     if not  lis:
#         return []
    
#     common_elements=set(lis[0])

#     for sublist in lis[1:]:
#         common_elements.intersection_update(set(sublist))

#     return list(common_elements)

# orginal_lists=[
#     [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]],
#     [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
# ]

# for i in orginal_lists:
#     print("Original list :")
#     print(i)
#     print("Common elements :")
#     print(commo(i))

    
# # WAPP to reverse a given list of lists.
# # so the thing  is to reverse the list of lists
# l=[['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]

# def rev(list):
#     return[i[::-1]  for i in list]


# print(rev(l))


# # WAPP to reverse the strings at  particular   location  or  specified place

# def rev_speci(num,start,end):
#     l=[]
#     for i in range(start,end+1):
#         l.append(num[i])
        

#     l.reverse()
    
#     for i in range(start,end+1):
#         num[i]=l[i-start]

#     return num

# original_lis=['a','b','c','d','e','f','g']
# start=0
# end=4
# print("original list",original_lis)
# print("Reversed at specified place",rev_speci(original_lis,start,end))


# # find the  value of the  x  i know  you can ??????? :)
# values=[[4,5,6,2],[44,7,2,3]]

# x=values[0][0]

# for row in range(0,len(values)):
#     for column in range(0,len(values[row])):

#         if x<values[row][column]:
#             x=values[row][column]

# print(x)




# values=[[4,5,6,2],[44,7,2,3]]

# for row in values:
#     row.sort()   
#     for element in row:
#         print(element,end=" ")        
#     print()
                        

# # WAPF to find the length of  the longest increasing sub-sequence in a list


# def longest_increasing_sub(nums):
#     n=len(nums)

#     arr=[1]*n
#     for i in range(1,n):
#         for j in range(i):
#             if nums[i]>nums[j]:
#                 arr[i]=max(arr[i],arr[j]+1)

#     return max(arr)

# nums=[10,20,30,40,50,60,70,80]
# nums=[]

# print(longest_increasing_sub(nums))


# WAPF  to finds all the permuatation of the members of a list.

# def permutation(lis):
#     if len(lis)==0:
#         return [[]]
#     elif len(lis)==1:
#         return [lis]
#     else:
#         r=[]
#         for i in range(len(lis)):
#                 for j in permutation(lis[:i]+lis[i+1:]):
#                      r.append([lis[i]]+j)
#     return r

# print(permutation([1,2,3,4]))
    

# def generate_permutations(lst):
#     n = len(lst)
#     c = [0] * n
#     result = [lst[:]]  # Start with the original list as the first permutation

#     i = 0
#     while i < n:
#         if c[i] < i:
#             if i % 2 == 0:
#                 lst[0], lst[i] = lst[i], lst[0]
#             else:
#                 lst[c[i]], lst[i] = lst[i], lst[c[i]]
#             result.append(lst[:])  # Append the generated permutation
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1

#     return result

# print(generate_permutations([1, 2, 3, 4]))
