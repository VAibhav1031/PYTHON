import  hashlib

"""This  is  all  about the md5 hashing"""

def hash_md5(input_string):
    hash_object=hashlib.md5(input_string.encode())
    return hash_object.hexdigest()




input_string="Hello"
print("MD5: ",hash_md5(input_string))

#************************************************************


"""This  is  all  about the sha1 hashing"""

def hash_sha1(input_string):
    hash_object=hashlib.sha1(input_string.encode())
    return hash_object.hexdigest()

input_string="Hello"
print("Sha1: ",hash_sha1(input_string))

# **********************************************************

"""This  is  all  about the sha256 hashing"""

def hash_sha256(input_string2):
    hash_object=hashlib.sha256(input_string.encode())
    return hash_object.hexdigest()

input_string="Hello"
print("Sha256: ",hash_sha1(input_string))


# *********************************************************


"""This  is  all  about the sha3_256 hashing"""
def hash_sha3_256(input_string2):
    hash_object=hashlib.sha3_256(input_string.encode())
    return hash_object.hexdigest()

input_string="Hello"
print("Sha3_256: ",hash_sha1(input_string))


