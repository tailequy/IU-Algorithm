#Functional Programming
#The lambda construct offers a way to define anonymous functions in Python
#lambda a : a + 13
#(lambda a : a + 13)(11)

#Creates a list of elements for which a function returns true
#list(filter(lambda x: x > p,L)) #filter out elements x > pivot:

aList=[11,59,26,17,2,1,25,9,3,15]
pivot=11
ans=(lambda L,p: list(filter(lambda x: x<= p,L)) +
                 list(filter(lambda x: x> p,L)))(aList,pivot)
print(ans)