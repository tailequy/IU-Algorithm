#Insertion Sort, O(n^2)
def insertionSort(aList):
    seqLen = len(aList)
    for index in range(1, seqLen):
        toInsert = aList[index]
        j = index
        while j > 0:
            if(toInsert >= aList[j-1]):
                break
            aList[j] = aList[j-1]
            j -= 1
        aList[j] = toInsert

aList = [12,3,22,44,15,13,7,45,77,33]
insertionSort(aList)
print("Insertion sort:")
print(aList)

#Bubble sort
def bubbleSort(aList):
    seqLen = len(aList)
    swapped = True
    for lastIndex in range(seqLen-1, 0, -1):
        if not swapped:
            break
        swapped = False
        for k in range(0, lastIndex):
            if aList[k] > aList[k + 1]:
                aList[k], aList[k + 1] = aList[k + 1], aList[k]
                swapped = True
aList = [12, 3, 22, 44, 15, 13, 7, 45, 77, 33]
bubbleSort(aList)
print("Bubble sort:")
print(aList)

#Selection Sort
def selectionSort(aList):
    seqLen = len(aList)
    for lastIndex in range(seqLen-1, 0, -1):
        maxIndex =0
        for k in range(1, lastIndex + 1):
            if aList[k] > aList[maxIndex]:
                maxIndex = k
        aList[lastIndex], aList[maxIndex] = aList[maxIndex],aList[lastIndex]
aList = [12,3,22,44,15,13,7,45,77,33]
selectionSort(aList)
print("Selection sort:")
print(aList)

#Quick sort, O(nlogn), the worst case: O(n^2)
def partition(aList, left, right):
    pivot = aList[left]
    i=left + 1
    j=right
    while True:
        while (i <= j) and (aList[i] <= pivot):
            i+=1
        while (i <=j) and (aList[j] >= pivot):
            j-=1
        if(i <= j):
            aList[i],aList[j] = aList[j],aList[i]
        else:
            break
    aList[left],aList[j]= aList[j],aList[left]
    return j
def qSort(aList, left, right):
    if (left >= right):
        return
    partIndex = partition(aList, left, right)
    qSort(aList, left, partIndex - 1)
    qSort(aList, partIndex + 1, right)
def quickSort(aList):
    seqLen = len(aList)
    qSort(aList, 0, seqLen-1)

aList = [12,3,22,44,15,13,7,45,77,33]
quickSort(aList)
print("Quick sort: ")
print(aList)

#Merge Sort, O(nlogn)
#mergesort is also a divide-and-conquer algorithm.
#The sequence is divided into two equal parts, which are then sorted recursively.
def merge(A,B,C):
    a=b=0
    la, lb, lc = len(A), len(B), len(C)
    while(a+b < lc):
        if((b==lb) or ((a < la) and (A[a]<B[b]))):
            C[a+b],a,b=A[a],a+1,b #Select from A
        else:
            C[a+b],a,b = B[b],a,b+1 #Select from B
    return C

def mergeSort(aList):
    seqLen = len(aList);
    if seqLen <= 1:
        return
    mid = seqLen//2
    lower = aList[:mid] #Copy lower half
    upper = aList[mid:] #Copy upper half
    mergeSort(lower) #Sort lower half
    mergeSort(upper) #Sort upper half
    aList = merge(lower,upper,aList)

aList = [12,3,22,44,15,13,7,45,77,33]
mergeSort(aList)
print("Merge sort:")
print(aList)

bList = [3,12,15,22,44,7,13,33,45,77]
merge(bList[:5],bList[5:10],bList)
print("Merge:")
print(bList)