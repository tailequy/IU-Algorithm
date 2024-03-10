#Data Stream Programming
#A “data stream” is a sequence of data items that are available one at a time.
# Python supports processing such streams of data by using a construct called the “generator”
# Generate the sequence of Fibonacci numbers.
def generateFib():
    one = 0
    other = 1
    while (1):
        yield one
        another = one + other
        one = other
        other = another

gen = generateFib()

def getLessThan(g, n):
    i=next(g)
    while i < n:
        print(i)
        i=next(g)
getLessThan(gen, 100)