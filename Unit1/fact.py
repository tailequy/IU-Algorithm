def fact(n):
    if (n==0):
        return 1
    else:
        return n*fact(n-1)
n = int(input("Input an integer: "))
print("n! =",fact(n))

#n! = 1*2*...*n
#0! = 1
#n! = n*(n-1)!

