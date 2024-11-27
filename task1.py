class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def AreaofRectangle(self):
        return self.a*self.b    
    
    def AreaofSquare(self):
        return self.a*self.a
    
    def printA(self):
        print("Class A")

class B(A):
    def printA(self):
        print("Class B")

class C(A):
    def printA(self):
        print("Class C")

# Example of Polymorphism 
obj1 = A(4,2)
print(f"Area of Rectangle : {obj1.AreaofRectangle()}")
print(f"Area of Square : {obj1.AreaofSquare()}")   
obj1.printA()     

# Example of Encapsulation
obj2 = B(10,20)
obj2.printA()

obj3 = C(2,3)
obj3.printA()
