class A():
    def __init__(self):
        print('A')
        super().__init__()

class B(A):
    def __init__(self):
        print('B')
        super().__init__()

class C(A):
    def __init__(self):
        print('C')
        super().__init__()

class D(B,C):
    def __init__(self):
        print('D1')
        super().__init__()
        print('D2')

D()
