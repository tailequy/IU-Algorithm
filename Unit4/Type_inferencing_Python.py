from random import randint
def typeCheck(num):
    if(num%2):
        a = 123
    else:
        a = "123"
    print(type(a))
typeCheck(randint(1,1000))