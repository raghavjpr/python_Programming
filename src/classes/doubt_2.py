class A():
    def __init__(self):
        print('A')
        super().__init__()

class B(A):
        print('B')
        super().__init__()

class C(A):
        print('C')

class D(A):
    pass

