#generates the prime factors of a natural number in Python
def generatePrimeFactors(num):
    fact = 2
    while fact * fact <= num:
        if num % fact:
            fact += 1
        else:
            num //= fact # divide with integral result
            yield fact
    if num > 1:
        yield num
#This is used as follows to generate the prime factors of 3,000
for i in generatePrimeFactors(3000):
    print(i)