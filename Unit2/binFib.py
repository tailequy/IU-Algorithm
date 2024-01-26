#Fibonacci numbers
#For all non-negative integers n as follows:
#fib(n) = n if 0 ≤ n < 2
#fib(n) = fib(n − 1) + fib(n − 2) if n ≥ 2
#Binary Recursive Fibonacci, the binary variant runs in exponential time
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return(fib(n-1)+fib(n-2))

print(fib(6))