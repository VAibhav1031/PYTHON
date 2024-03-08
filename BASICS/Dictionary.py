# Problems on Dictionary

# # 1.
# #  Write a Python program to find the key 
# # of the maximum value in a dictionary.
# # Sample Output:

# # Original dictionary elements:
# # {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# # Finds the key of the maximum and minimum value of the said dictionary:
# # ('Roxanne', 'Theodore')

# # Solution
# # Maximum Value And Minimum Value

# my_dict={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# key_max=max(my_dict.keys(),key=(lambda k:my_dict[k]))
# key_min=min(my_dict.keys(),key=(lambda k:my_dict[k]))

# print("Maximum Value",my_dict[key_max])
# print("Maximum Value",my_dict[key_min])


# # 2.
# # Write a Python program to create a flat list of all the values in a flat dictionary.
# # Sample Output:
# # Original dictionary elements:
# # {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# # Create a flat list of all the values of the said flat dictionary:
# # [19, 20, 21, 20]



# # solution
# mydict1={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# d=mydict1.values()
# print(list(d))

# # 3.
# #  Write a Python program to create a flat list of all the keys in a flat dictionary.
# # Sample Output:
# # Original dictionary elements:
# # {'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# # Create a flat list of all the keys of the said flat dictionary:
# # ['Theodore', 'Roxanne', 'Mathew', 'Betty']

# # solution:
# mydict1={'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# d=mydict1.keys()
# print(list(d))


# #4
# #.Write a Python program to transform a dictionary into a list of tuples.
# #Sample Output:
# #Original Dictionary:
# #{'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# #Convert the said dictionary to a list of tuples:
# #[('Red', 1), ('Green', 3), ('White', 5), ('Black', 2), ('Pink', 4)]

# #solution:
# mydict={'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# d=mydict.items()
# print(list(d))


## 5.
## Write a Python program to combine two lists into a dictionary. The elements of the first one serve as keys and the elements of the second one serve as values. Each item in the first list must be unique and hashable.
##Sample Output:
## Original lists:
##['a', 'b', 'c', 'd', 'e', 'f']
##[1, 2, 3, 4, 5]
##Combine the values of the said two lists into a dictionary:
##{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


##solution:
# l1=['a', 'b', 'c', 'd', 'e', 'f']
# l2=[1, 2, 3, 4, 5]
# d=dict(zip(l1,l2))
# for i,k in d.items():
#     print(i,':',k)
# print(d)



##6.
# # Write a Python program to find all keys in a dictionary that have the given value.
# #Sample Output:
# #Original dictionary elements:
# #{'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# #Find all keys in the said dictionary that have the specified value:
# #['Roxanne', 'Betty']

# # Solution
# def test(dict,val):
#     return[key for key,value in dict.items() if value==val]


# dic={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}

# print(test(dic,20))

# My Way:
# d={'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
# values=[]
# for i,j in d.items():
#     values.append(d[i]['age'])
#     # print(d[i]['age'])

# keys=list(d.keys())
# print("Values ",values)
# print("Keys ",keys)
# d1={}
# for i,k in  zip(keys,values):
#     d[i]=k
    
# print(d)


# Some edit in my way>
# def test(obj,fn):
#     return dict((k,fn(v)) for k ,v in obj.items())

# print("The original dictionary:")
# d={'Theodore': {'user': 'Theodore', 'age': 45}, 'Roxanne': {'user': 'Roxanne', 'age': 15}, 'Mathew': {'user': 'Mathew', 'age': 21}}
# print(d)


# print(test(d,lambda x:x['age']))

# 6.





# Solution:
# 


# def test(d):
#     values=[]
#     for i,j in d.items():
#         values.append(d[i]['age'])
#     return values

# d = {
#     'Theodore': {'user': 'Theodore', 'age': 45},
#     'Roxanne': {'user': 'Roxanne', 'age': 15},
#     'Mathew': {'user': 'Mathew', 'age': 21}
# }

# print(test(d))


# # 7.Invert the  dictionary 
# # def invert_dict(d):
# #     return{v:k for k,v in d.items()}

# # d={'Theodore': 45, 'Roxanne': 15, 'Mathew': 21}

# # print(invert_dict(d))

# # find the  value of nested dicitionary key
# # simple nested
# nested_dict1 = {
#     'key1': {
#         'nested_key1': 'nested_value1',
#         'nested_key2': 'nested_value2'
#     },
#     'key2': {
#         'nested_key3': 'nested_value3',
#         'nested_key4': 'nested_value4'
#     }
# }

# print(nested_dict1)
# print("The value of the nested_key4 ",nested_dict1["key2"]["nested_key4"])

# print()

# # Little more complex
# nested_dict = {
#     'person1': {
#         'name': 'John',
#         'age': 30,
#         'address': {
#             'street': '123 Main St',
#             'city': 'New York',
#             'zip': '10001'
#         }
#     },
#     'person2': {
#         'name': 'Alice',
#         'age': 25,
#         'address': {
#             'street': '456 Elm St',
#             'city': 'Los Angeles',
#             'zip': '90001'
#         }
#     }
# }

# print(nested_dict)
# # what is the city where 'person1' lives?
# print(nested_dict['person1']['address']['city'])

# #8.

# # Write a Python program to group the elements of a given list based on the given function.
# # Sample Output:
# # Original list & function:
# # [7, 23, 3.2, 3.3, 8.4] Function name: floor:
# # Group the elements of the said list based on the given function:
# # {7: [7], 23: [23], 3: [3.2, 3.3], 8: [8.4]}
# # Original list & function:
# # ['Red', 'Green', 'Black', 'White', 'Pink'] Function name: len:
# # Group the elements of the said list based on the given function:
# # {3: ['Red'], 5: ['Green', 'Black', 'White'], 4: ['Pink']}

# import math

# li=[7, 23, 3.2, 3.3, 8.4]
# def floor(li):
#     result={}
#     for num in li:
#         key=math.floor(num)
#         if key not in result:
#             result[key]=[num]
#         else:
#             result[key].append(num)

#     return result

# print(floor(li))        

# li=['Red', 'Green', 'Black', 'White', 'Pink']
# def string_len(li):
#     result={}
#     for word in li:
#         key=len(word)
#         if key not in result:
#             result[key]=[word]
#         else:
#             result[key].append(word)

#     return result

# print(string_len(li))


# # 9
# # Write a Python program to combine two or more dictionaries, creating a list of values for each key.
# # Sample Output:
# # Original dictionaries:
# # {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# # {'x': 300, 'y': 'Red', 'z': 600}
# # Combined dictionaries, creating a list of values for each key:
# # {'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}
# # li1={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# # li2={'x': 300, 'y': 'Red', 'z': 600}
# def stu(list1,list2):
#     result={}
    # for i,j in li1.items():
    #         if i not in result:
    #             result[i]=[j]
    #         else:
    #             result[i].append(j)
#     for i,j in li2.items():
#             if i not in result:
#                 result[i]=[j]
#             else:
#                 result[i].append(j)
#     return result

# print(stu(li1,li2))


# sd={8: ['Ora Mckinney', 'Mathew Gilbert'], 7: ['Theodore Hollandl', 'Mae Fleming', 'Ivan Little']}

# def js(l):
#     return {tuple(v):k for k,v in l.items()}

# print(js(sd))


# students = {
#   'Ora Mckinney': 8,
#   'Theodore Hollandl': 7,
#   'Mae Fleming': 7,
#   'Mathew Gilbert': 8,
#   'Ivan Little': 7,
# }

# def invert(li):
#      return{v:k for k,v in li.items()}

# print(invert(students))
# def fu(li):
#         result={}
#         for i,j in li.items():
#             if i not in result:
#                 result[i]=[j]
#             else:
#                 result[i].append(j)


# print(fu(students))



# d={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

# print(len(d))

# # To  find the length of the whole dictionary

# def length(li):
#     t=0
#     for i,j in li.items():
#         t+=len(i)+len(j)

#     return t

# print(length(d))

# # to find the  length of the values only  not key 

# def lengt(li):
#     t=0
#     for i,j in li.items():
#         t+=len(j)

#     return t

# print(lengt(d))



#  Write a Python program to convert a given list of lists to a dictionary.
# Original list of lists:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}


# List of list    to  the 
# h=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# def convert(li):
#     return {item[0]:item[1:] for item in li}

# print(convert(h))

# ll=[{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]

# def dict_to_lilistst(ll):

#     return [list(item.values()) for item in ll]


# print(dict_to_lilistst(ll))



# # write the python prorgaram to dins the shortest list of the values
# # for the keys in a given dictionary

# s={'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} 
# def shortest_list(dic):
#     return[x for x,y in dic.items() if len(y)==1]


# print(shortest_list(s))


# #  Write a Python program to count the frequency of a dictionary.
# # Original Dictionary:
# from collections import Counter
# s={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# def freq(dic):
#     d={}
#     for value in dic.values():
#         if value in d:
#             d[value]+=1
#         else:
#             d[value]=1

#     return d
# print(freq(s))


# # We can  also use the counter in this to do so

# def freq1(dic):
#     s=Counter(dic.values())

#     return s
# print(freq1(s))
             


# Write a Python program to find the specified number of maximum values in a given dictionary.
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:
# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']

# s={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# def specif_max(dic,m):
#     max_values=sorted(dic,key=dic.get,reverse=True)[:m]
#     return max_values

# print(specif_max(s,1))


# # write  a python program  to filrer evene numbers from a dictionary of values
# # solution
# import itertools
# s={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# def comb(ls):
#     result=list(map(dict,itertools.combinations(ls.items(),2)))
#     return result
# print(comb(s))



# # 57. Write a Python program to filter even numbers from a dictionary of values.
# # Original Dictionary:
# # {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# # Filter even numbers from said dictionary values:
# # {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# # Original Dictionary:
# # {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# # Filter even numbers from said dictionary values:
# # {'V': [], 'VI': [], 'VII': [2]}

# s1={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# def even_ele(li):
    
#     return{k:[x for x in v if x%2==0] for k,v in li.items()}

# print(even_ele(s))
# print(even_ele(s1))

# # Write a Python program to convert a dictionary into a list of lists.
# # Original Dictionary:
# # {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# # Convert the said dictionary into a list of lists:
# # [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# # Original Dictionary:
# # {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# # Convert the said dictionary into a list of lists:
# # [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]


# # solution
# ll={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# ll1={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# def list_of_list(li):
#     return[[k,v] for k,v in li.items()]

# print(list_of_list(ll))
# print()
# print(list_of_list(ll1))


#  Write a Python program to access dictionary key's element by index.
# Expected Output:
# physics
# math
# chemistry

# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# D={1:"Apple",2:"Banana",3:"Grape",4:"Orange"}
# print(D[1])

# print(list(num)[0])


# # find the  depth of the  dictionary 
# # depth means  the number of nested dictionary 
# # WE basically use the recursive method to do 

# # solution
# def dict_depth(d):
#     if isinstance(d, dict):
#         return 1 + (max(map(dict_depth, d.values())) if d else 0)
#     return 0


# dic = {'a':1, 'b': {'c': {'d': {}}}}
# print(dict_depth(dic))

# ll=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# def extract(li):
#     return [d["Science"] for d in li]
# print(extract(ll))
# print()
# def extract(li):
#     return [d["Math"] for d in li]
# print(extract(ll))




# d={'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

# def chane(li):
#     return [1+x for x in li['Math']]

# print(chane(d))


# #  A Python dictionary contains List as a value. Write a Python program to clear the list values in the said dictionary.
# # Original Dictionary:
# # {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# # Clear the list values in the said dictionary:
# # {'C1': [], 'C2': [], 'C3': []}

# k={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# def clear_list(l):
#     return{k:[] for k,v in l.items()}

# print(clear_list(k))


# Write a Python program to convert string values of a given dictionary into integer/float datatypes.
# Original list:alues of a given dictionary into integer/float datatypes.
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q':

# Solution
# solution:

# d=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# def str_int(li):
#     return[{i:int(j) for i,j in d.items()} for d in li]
# print(str_int(d))

# d=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# def str_int(li):
#     return[{i:float(j) for i,j in d.items()} for d in li]
# print(str_int(d))








