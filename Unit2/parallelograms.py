# Example of object-oriented programming in Python
class Parallelogram:
    def __init__(self, p, q):
        self.first = p
        self.second = q
        self.third = p
        self.fourth = q

    def perimeter(self):
        return(self.first + self.second + self.third+self.fourth)
# The Rectangle class inherits the perimeter method from the base class Parallelogram
class Rectangle(Parallelogram):
    def __init__(self, p, q):
        super().__init__(p,q)

    #The Rectangle class extends the base class Parallelogram with an area method
    def area(self):
        return(self.first*self.second)

#the Square class inherits the perimeter method from the base class Parallelogram
class Square(Rectangle):
    def __init__(self, p):
        super().__init__(p,p)
    #The Square class area method overrides the area method from the Rectangle class
    def area(self):
        return(self.first*self.first)

P=Parallelogram(3,4)
print(P.perimeter())

R=Rectangle(3,4)
print(R.perimeter())
print(R.area())

S=Square(5)
print(S.perimeter())
print(S.area())