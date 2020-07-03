class SingletonMeta(type):
    def __init__(self, *args, **kwargs):
        self._instance = None
        super(SingletonMeta, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(SingletonMeta, self).__call__(*args, **kwargs)
        return self._instance

class Person(metaclass=SingletonMeta):

    def __init__(self):
        self.name = 'kiennt'
        self.age = 26

class Dog(object):
    def __init__(self):
        self.name = "ruoc"
        self.age = 5
    
a = Person()
print (a.name) # kiennt
print (a.age) # 26
b = Person()
print (b == a) # True
print (id(a), id(b))
x = Dog()
print (x.name) #
print (x.age) # 
y = Dog()
print (x == y)
print(id(x), id(y))

print (isinstance(a, object))