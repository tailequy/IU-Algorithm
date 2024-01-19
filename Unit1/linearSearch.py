import random
def linSearch(numList, keyValue):
    index = 0
    while(index < len(numList)):
        if(keyValue == numList[index]):
            return index
        index += 1
    return -1

numlist = random.sample(range(0, 100), 10)
print("List of numbers:",numlist)
value = eval(input('Enter a number:'))
if (linSearch(numlist, value)!=-1):
    print("Found")
else:
    print("Not found")