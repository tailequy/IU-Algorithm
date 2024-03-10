#Namespace
x=1
def A():
    y=2
    def B():
        z=3
        print(vars()) #vars() returns the whole dictionary
        print(dir())  # dir() returns the keys
    B()
    print(vars())
    print(dir())
A()