# class A:
#     def method(self):
#         print("A.method")

# class B(A):
#     def method(self):
#         print("B.method")

# class C(A):
#     def method(self):
#         print("C.method")

# class D(B, C):
#     pass

# print(D.mro())

class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        super().method()
        print("B.method")

class C(A):
    def method(self):
        super().method()
        print("C.method")

class D(B, C):
    def method(self):
        super().method()
        print("D.method")

# Usage
d = D()
d.method()



print()
print()

class A:
    def foo(self):
        print("Method foo() from class A")

class B(A):
    def foo(self):
        super().foo()  # Calls foo() from class A using super()

class C(A):
    def foo(self):
        super().foo()  # Calls foo() from class A using super()

class D(B, C):
    pass

d = D()
d.foo()  # Output: Method foo() from class A



# MRO resolves the order of classes being inherited by multiple  classes , BAsically it  gives the   order  of heirarchy in which  class is inherited  by using the  c3 Linearlization algorithm
