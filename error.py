# def add(a,b):
#     return a+b

# print(add(10,20))

# numb1=10


# # this  will give  us error  beacuse  we are giving  an string number2 input

# try:
#     numb2=input("Enter the number")
#     print(add(numb1,numb2))

# except:
#     num2=int(numb2)
#     print("srry we cant take str for addition")
#     print(add(numb1,num2))


# try:
#     file=open('testfile.txt','w')
#     file.write("written a line")

# except TypeError:
#     print("ther is an type error")

# except OSError:
#     print("There is an OS error")

# except :
#     print("ALL other Exceptions")
# finally:
#     print("I always run")


# def ask_for_int():

#     while True:
#         try:
#             result=int(input("Please provide number:"))

#         except:
#             print("Whoops!! that is not a number")
#             continue
#         else:
#             print("Yes !! thank you")
#             break
#         finally:
#             print("End of try/except/finally")
#             print("I always  run at the end !")

# ask_for_int()


# # problem1:

# for i in ['a','b','c']:
#     try:
#         print(int(i)**2)
#     except ValueError:
#         print(f"Cannot convert '{i}' to an integer.")

# # problem2:

# x=5
# y=0

# try:
#   z=x/y
#   print(z)
# except ZeroDivisionError:
#     print("cannot divide the number by 0")

# finally:
#     print("All Done")

# problem 3:

# def ask():

#     while True:
#         try:
#             num=int(input("Enter the number:"))
#             sq=num**2
#             print(sq)
#         except:
#             print("An occured! Please try again!")
#         else:
#             print("Thank you, your number squared is:",sq)
#             break


# ask()     

        




