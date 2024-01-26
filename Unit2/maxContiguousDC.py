#Maximum Contiguous Subarray Problem
# Divide-and-conquer algorithm for the Maximum Contiguous Subarray Problem
#T(n) = O(nlogn) because there is O(n) amount of work involved in each of
# O(logn) levels of recursion.
#1. Divide the array into two parts.
#2. Compute the sum of the Maximum Contiguous Subarray residing exclusively on the left.
#3. Compute the sum of the Maximum Contiguous Subarray residing exclusively on the right.
#4. Compute the sum of the Maximum Contiguous Subarray that crosses the boundary.
#5. Return the maximum of the three sums computed.
def maxContiguousSubseqDC(A, low, high):
    if(low == high): #single element
        return max(0,A[low]) #if negative return 0
    mid=(low+high)//2
    #find max crossing subsequence to the left
    subseqSum = 0
    maxLeftSum = 0
    for i in range(mid, low-1, -1):
        subseqSum += A[i]
        maxLeftSum = max(maxLeftSum, subseqSum)
    # find max crossing subsequence to the right
    subseqSum = 0
    maxRightSum = 0
    for i in range(mid+1, high + 1):
        subseqSum += A[i]
        maxRightSum = max(maxRightSum, subseqSum)
    # find max subsequence exclusively to the left
    left = maxContiguousSubseqDC(A, low, mid)
    # find max subsequence exclusively to the right
    right = maxContiguousSubseqDC(A, mid+1, high)
    print("low, mid, high, left, right, maxLeft, maxRight", low, mid, high,
          left, right, maxLeftSum, maxRightSum)
    return (max(left, maxLeftSum + maxRightSum, right))

#Test
listA=[-6, -22, 1, 6, -5, 3, 4]
print("maxSumDC=", maxContiguousSubseqDC(listA,0,6))

