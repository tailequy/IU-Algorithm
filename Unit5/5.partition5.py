#Logic Programming
#kanren package: a library within PyPi that simplifies ways of making business logic out of code
#import os
#os.system('pip install kanren')
from kanren import run, eq, membero, var, conde
from kanren.arith import lt,gt
x =var()
L=[11,59,26,17,2,1,25,9,3,15]
pivot = 11

#First, we collect all elements less than the pivot in list a,
# elements equal to the pivot in b,
# and elements greater than the pivot in c.
# We concatenate the results into list d.
a=run(0,x,(membero, x, L),(lt,x,pivot))
b=run(0,x,(membero, x, L),(eq,x,pivot))
c=run(0,x,(membero, x, L),(gt,x,pivot))
d=run(0,x,(membero,x,a+b+c))
print(d)