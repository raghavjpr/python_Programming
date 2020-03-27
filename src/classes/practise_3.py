class A():
    def __init__(self):
        print('A')
        super().__init__()

class B(A):
        print('B')

class C(A):
        print('C')

class D(A):
    pass

    
print(type(D()))
print(type(C()))
print(type(B()))
print(type(A()))




