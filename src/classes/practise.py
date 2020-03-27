class MyClass:
    myClassVar = "hello"

    def method(self):
        #self.myClassVar = "Raghav"
        print('instance method called', self)

    @classmethod
    def classmethod(cls):
        cls.myClassVar = "World"
        print('class method called', cls)

    @staticmethod
    def staticmethod():
        print('static method called')


obj = MyClass()

print (obj.myClassVar)
obj.method()
print (obj.myClassVar)

MyClass.method(obj)
# MyClass.method(obj22)

print (obj.myClassVar)
obj.classmethod()
print(MyClass.myClassVar)
print (obj.myClassVar)


obj.staticmethod()
# obj.staticmethod(xyz)
# obj.staticmethod(1)
