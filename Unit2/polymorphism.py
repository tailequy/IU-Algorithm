#The len function in Python works for several types, including ranges, strings, lists, tuples,
#sets, and dictionaries
A = range(0, 5) #range
print(len(A))

B= [2,3,4,5] #list
print(len(B))

C= (4, 5,6) #tuple
print(len(C))

D = {4,5,6,7,8,9} #set
print(len(D))

E = {'a':2, 'b':3} #dictionaries
print(len(E))

#The + operator works for a variety of types, such as strings, numeric types, lists, and
#tuples, but both operands must be of the same type
a = 23
b = 45
print(a+b) # 68

a = "abc"
b = "def"
print(a+b) # abcdef

a = [1,2,3]
b=[4,5]
print(a+b) # [1, 2, 3, 4, 5]

a = (1,2,3)
b = (3,4,5)
print(a+b) # (1, 2, 3, 3, 4, 5)
