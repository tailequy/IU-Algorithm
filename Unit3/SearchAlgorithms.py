#Sequential Search
#unordered list, O(n)
def linearSearch(numList, keyValue):
    index = 0
    listLen = len(numList)
    while(index < listLen):
        if(keyValue == numList[index]):
            return index
        index += 1
    return -1
#Ordered list, O(n)
def orderedLinearSearch(numList, keyValue):
    index = 0
    success = False
    stop = False
    listLen = len(numList)
    while index < listLen and not success and not stop:
        if (keyValue == numList[index]):
            success = True
        else:
            if (numList[index] > keyValue):
                stop = True
            else:
                index += 1
    return success

#Binary search, O(log n)
def binarySearch(numList, keyValue):
    left = 0
    right = len(numList) - 1
    found = -1
    while left <= right:
        mid = (left + right) // 2
        if numList[mid] == keyValue:
            found = mid
            break
        else:
            if keyValue < numList[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return found

numList = [3, 6, -10, 7, 9, 12, 15, 30]
orderednumList = [-10, 3, 6, 7, 9, 12, 15, 30]
if linearSearch(numList,9)!=-1:
    print("Found")
else:
    print("Not found")

if orderedLinearSearch(orderednumList, 9)==True:
    print("Found")
else:
    print("Not found")

if binarySearch(orderednumList,16)!=-1:
    print("Found")
else:
    print("Not found")