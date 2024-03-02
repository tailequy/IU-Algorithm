#find the highest power of a given number that is a factor of a second given number
#eg. powersOfFactor(40, 2) = 3
def powersOfFactor(num, fact):
    if(num == fact):
        return 1
    elif num % fact == 0:
        return(powersOfFactor(num//fact,fact) + 1)
    return 0

