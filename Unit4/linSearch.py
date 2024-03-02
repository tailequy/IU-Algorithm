aList = [23,34,2,13,11,-1,33,-44]
def linSearch(numList, keyValue):
    """Search for keyValue in numList.
    Args:
    numList: a list of values
    keyValue: a value being searched for in numList.

    Returns:
    index of keyValue in numList if found.
    -1 otherwise.
    """
    index = 0
    while(index < len(numList)):
        if(keyValue == numList[index]):
            return index
        index += 1
    return -1

print(linSearch(aList,11))
help(linSearch)

#Save to HTML file
#python -m pydoc -w linSearch