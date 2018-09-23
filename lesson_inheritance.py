class A:
    def __init__(self):
        self.attr1 = "attata"
        self.attrX = "attataX"


    def foo(self):
        print('Hello from A.foo()')

class A1(A):
    pass


class A2(A):
    pass

class B(A1, A2):


    def __init__(self):
        super().__init__()
        self.attr1 = 'atatat1'
        self.attr2 = 'atatat2'

b = B()
b.foo()
print(b.attr1)
print(b.attr2)
print(b.attrX)

