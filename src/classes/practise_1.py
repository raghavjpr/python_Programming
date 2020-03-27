class First():
    def __init__(self):
        print("first")
        super().__init__()

class Second():
    def __init__(self):
        print("second")

class Third(First, Second):
    def __init__(self):
        print("third")
        super().__init__()

Third()
