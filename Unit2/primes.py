# Compute the prime factors of a natural number num
def primeFactors (num, fact):
    if num < fact*fact:
        return [num]
    if num % fact == 0:
        return [fact] + primeFactors (num // fact, 2)
    return primeFactors (num, fact + 1)

#returns the prime factors in a list
n = int(input("Input a number: "))
print(primeFactors(n,2))