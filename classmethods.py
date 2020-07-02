class A:
    
    def __init__(self, xinchao):
        self.xinchao = xinchao
        self.tambiet = "tambiet"
    def __str__(self):
        return "day la str"
    def __repr__(self):
        return "heloo"
    
class B(A):
    @property
    def tambiet1(self):
        return self.tambiet
    @tambiet1.setter
    def tambiet1(self, tambiet):
        self.tambiet = tambiet

    @tambiet1.deleter
    def tambiet1(self):
        del self.tambiet
        print ("da xoa")
a = A("chao")
b = B("xiao")
print (a.xinchao)
print (b.xinchao)
print (a.__dict__)
print (a.__repr__)

class C(object):
    def __init__(self):
        self._x = "dfsdfd"

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

class Line:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_mult(self, x):
        return self.length*x
    @classmethod 
    def from_inches(cls, length_in, width_in):
        length = float(length_in)*2.54 
        width = float(width_in)*2.54 
        return cls(length, width)
l = Line.from_inches(3, 1) 

print (l.length) #returns 7.62
print (l.width)

def timeit(func, *args, **kwargs):
    def inner(*args, **kwargs):
        import time
        start = time.time()
        retval = func(*args, **kwargs)
        finish = time.time() - start
        return finish, retval
    return inner

#@timeit
def adder(a):
   return sum(a)

@timeit
def adder1(a):
   return sum(a)
print (timeit(adder)(range(10)))
print (adder1(range(10)))
