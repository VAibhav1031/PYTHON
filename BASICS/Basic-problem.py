# *******************************************************************************************
# list1 = [54, 44, 79, 91, 41]

# def print_options():
#     print("******************************************************************")
#     print("OPTIONS:")
#     print("\t1. Remove an element at a specific index")
#     print("\t2. Insert an element at a specific index")
#     print("\t3. Append an element to the end of the list")
#     print("\t4. Print the current list")
#     print("\t5. Quit")
#     print("******************************************************************")

# def list_ma():
#     while True:
#         print_options()
#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             try:
#                 index = int(input("Enter the index of the element to remove: "))
#                 if 0 <= index < len(list1):
#                     list1.pop(index)
#                     print("Element removed successfully.")
#                 else:
#                     print("Index out of range. Please enter a valid index.")
#             except ValueError:
#                 print("Invalid input. Please enter a valid integer index.")
        
#         elif choice == "2":
#             try:
#                 index = int(input("Enter the index to insert the element: "))
#                 value = int(input("Enter the value to insert: "))
#                 if 0 <= index <= len(list1):
#                     list1.insert(index, value)
#                     print("Element inserted successfully.")
#                 else:
#                     print("Index out of range. Please enter a valid index.")
#             except ValueError:
#                 print("Invalid input. Please enter valid integer values.")
        
#         elif choice == "3":
#             try:
#                 value = int(input("Enter the value to append: "))
#                 list1.append(value)
#                 print("Element appended successfully.")
#             except ValueError:
#                 print("Invalid input. Please enter a valid integer value.")
        
#         elif choice == "4":
#             print("Current list:", list1)
        
#         elif choice == "5":
#             print("Exiting program.")
#             break
        
#         else:
#             print("Invalid choice. Please select a valid option.")

# list_ma()



# **********************************************************************************

# # divide the list into the  three part  an d display them with reverse form also

# # 1
# sample_list=[11,45,8,23,14,12,78,45,89]
# for i in range(0,len(sample_list),3):
    
#     c1=sample_list[i:i+3]
#     print(f"Chunk {i+1}",c1)
#     c1.reverse()
#     print("After reversing it ",c1)
#     print()


# # 2
# lenght=len(sample_list)
# chunk_size=int(lenght/3)
# start=0
# end=chunk_size

# for i in range(3):
#     indexes=slice(start,end)
#     list_chunk=sample_list[indexes]
#     print(f"Chunk {i+1}",list_chunk)

#     print("Afer reversing it ",list(reversed(list_chunk)))

#     start=end # now it update the end  as the start  for next chunk
#     end+=chunk_size # this will move end pointer or size to next three





# sample_list=[11,45,8,11,23,45,51,89]
# d={}
# for i in sample_list:
#     if i in d:
#         d[i]+=1

#     else:
#         d[i]=1

# print(d)

# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
# zipped=zip(first_list,second_list)
# # print(list(zipped))
# # print(set(zipped))   ## comment thing out to check things

# # When you zip two lists together and convert the result to a list, you exhaust the iterator. 
# # As a result, when you try to convert the iterator to a set afterward, it's empty because it has
# # already been consumed

# #  we can store the  zipped function to  can use it with others

# zipped_list = list(zipped)
# print(zipped_list)

# # Convert the list of zipped pairs to a set
# zipped_set = set(zipped_list)
# print(zipped_set)




# first_set = {23,42,65,57,78,83,29}
# second_set = {57,83,29,67,73,43,48}
# s=set()
# for i in first_set:
#     for j in second_set:
#         if i==j:
#             s.add(i) 

# print("Intersection set : ",s)
# print("First set after removing common element:",first_set-s)

# def intersection(l:set,l1:set) ->None:
#     s=set()
#     for i in l:
#         for j in l1:
#             if i==j:
#                 s.add(i) 
#     print("Intersection(common) set:",s)
#     return l-s

# if __name__=="__main__":
#     l:set={23, 42, 65, 57, 78, 83, 29};print("First set:",l)
#     l1:set={57, 83, 29, 67, 73, 43, 48};print("First set:",l1)
#     difference_set = intersection(l, l1)
#     print("Set difference:", difference_set)


# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}
# for i in first_set:
#     for j in second_set:
#         if i==j:
#             print("First set is subset of second set - True")
#         else:
#             print("First set is subset of second set - False")


# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}

# # Check if every element in the first set exists in the second set
# is_subset = all(element in second_set for element in first_set)
# is_superset=all(element in first_set for element in second_set)

# print("First set is subset of second set -", is_subset)
# print("Second set is subset of First set -", is_superset)

# # 
# all() is a built-in Python function that returns True if 
# all elements in an iterable are true, and False otherwise. 


# ****
#  Iterate a given list and check if a given element exists as a key’s value 
# in a dictionary. If not, delete it from the list

# roll_number=[47,64,69,37,76,83,95,97]
# sample_dict={'John ':47,'Emma':69,"kelly":76,"Jason":97}

# # for value in sample_dict.values():
# #     if value in roll_number:
# #         roll_number.remove(value)


# # print(roll_number)

# sample_values=sample_dict.values()
# print(sample_values)
# s=[x for x in roll_number if x not in sample_values]
# print(s)



# #  Get all values from the dictionary and add them to a list but don’t add duplicates

# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# val=speed.values()
# print(list(set(val)))


# Remove duplicates from a list and create a tuple and find the minimum and maximum number


# sample_list=[87,45,41,65,94,41,99,94]
# list=list(set(sample_list))
# tu=tuple(list)
# print("Unique items: ",list )
# print("Tuple : ",tu)
# print(min(tu))
# print(max(tu))

# #  Reverse the list

# list1=[100,200,300,400,500,600]
# # list1.reverse()
# print(list1)

# list1=list1[::-1]
# print(list1)


# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# # new=[]
# # for i,j in zip(list1,list2):
# #         l=i+j
# #         new.append(l)
# new=[i+j for i,j in zip(list1,list2)]
# print(new)


# numbers=[1,2,3,4,5,6,7,8]
# l=[x*x for x in numbers ]  # we can  use the  looops  also  
# print(l)

# list1=["hello","Take"]
# list2=["Dear","Sir"]
# new=[]
# for i in list1:
#     for j in list2:
#         l=i+" "+j
#         new.append(l)

# print(new)

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for i,j in  zip(list1,list2[::-1]):
#     print(i,j)


# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# li=list(filter(lambda x:isinstance(x,str) and x!="",list1))
# print(li)

# list1=[10,20,[300,400,[5000,6000],500],30,40]

# list1[2][2].append(7000)
# print(list1)

# *******
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list=["h","i","j"]
# list1[2][1][2].extend(sub_list)
# print(list1)


# list1=[5,10,15,20,25,50,20]
# index=list1.index(20)

# list1[index]=200
# print(list1)

# list1=[5,10,15,20,25,50,20]
# def remove_value(list,val):
#     return[i for i in list if i!=val]

# res = remove_value(list1, 20)
# print(res)

# keys=["Ten","Twenty","Thirty"]
# values=[10,20,30]
# res_dict=dict(zip(keys,values))
# print(res_dict)

# d=dict()
# for i in range(len(keys)):
#     d.update({keys[i]:values[i]})

# print(d)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3=dict1.copy()
# dict3.update(dict2)

# print(dict3)


# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# res=dict.fromkeys(employees,defaults)
# print(res)

#  to have the  same  values for the  keys

# x = [
#     'a',
#     'b',
#     {
#         'foo': 1,
#         'bar':
#         {
#             'x' : 10,
#             'y' : 20,
#             'z' : 30
#         },
#         'baz': 3
#     },
#     'c',
#     'd'
# ]
# print(x[2]['bar']['z'])
# d={"hey":200,"bol":542}
# d1={}
# d1.update(d)
# print(d1)

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]

# for key in keys:
#     sample_dict.pop(key)

# print(sample_dict)

# sample_dict={'a':100,'b':200,'c':300}
# val=sample_dict.values()
# if 200 in val:
#     print("200 present in a dict")



# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sample_dict.pop("city")
# sample_dict["location"]="New York"

# print(sample_dict)


# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# val=sample_dict.values()
# val=min(sample_dict)
# print(val)


# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict['emp3']['salary']=8500
# print(sample_dict)

# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# sample_set.update(sample_list)
# print(sample_set)


# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.intersection(set2))

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.union(set2))

# print("Set1 ",set1-set2)

# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10,20,30})
# print(set1)

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.symmetric_difference(set2))

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# print(set1.intersection(set2))

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set1.symmetric_difference_update(set2)
# print(set1)

# when we use the _update statement  basically  it modifies the 
# original sets rathere creating the  new one  which normal without
# _update one  do 


# d={"Red":1,"Green":2,"Blue":3}
# for color_key,value in d.items():
#     print(color_key,"corresponds to",d[color_key])

# d={"Red":1,"Green":2,"Blue":3}
# for color_key,value in d.items():
#     print(color_key,"corresponds to",value)


# d={
#    0:10,
#    11:20,
#    21:30
# }

# d.update({31:40})
# print(d)
# print(d.get(51,-1))

# myDict = {'a':1,'b':2,'c':3,'d':4}
# print(myDict)
# if 'e' in myDict:
#     del myDict['e']

# print(myDict)

# # Basic dictionary exmpless
# color_dict={
#     'red':"#FF0000",
#     "Green":"#08000",
#     "BlacK":"#00000",
#     "White":"#FFFFF"

# }


# for key in sorted(color_dict):
#     print("%s: %s" % (key,color_dict[key]))


# my={
#     'x':500,
#     'y':5874,
#     'z':560
# }
# key_max=max(my.keys(),key=(lambda k:my[k]))
# key_min=min(my.keys(),key=(lambda k:my[k]))

# print("Maximum Value",my[key_max])
# print("Minimum Value",my[key_min])


# fruits = {}
# fruits["apple"] = 1
# fruits["mango"] = 2
# fruits["banana"] = 4

# # Use in.
# if "mango" in fruits:
#     print("Has mango")
# else:
#     print("No mango")

# # Use in on nonexistent key.
# if "orange" in fruits:
#     print("Has orange")
# else:
#     print("No orange")


# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# # dic4.update(dic1,dic2,dic3) # this  will give you  error  cause 
#                             # it takes only one  argument 
# print(dic4)



# for d in (dic1,dic2,dic3):
#     dic4.update(d)

# print(dic4)