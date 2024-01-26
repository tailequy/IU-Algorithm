#Maximum Contiguous Subarray Problem
# Sum(i, j) = A[i] if j = i
# Sum(i, j) = Sum(i,j− 1) + A[j] if i < j < n
# Complexity: O(n^2)
def maxContiguousSubseqDP(A):
    maxSum = 0
    n = len(A)
    for i in range(0,n):
        subseqSum = 0
        for j in range(i, n):
            subseqSum += A[j]  # Compute Sum(i,j)
        maxSum = max(maxSum, subseqSum)
    print("maxSumDP =", maxSum)
listA = [-6, -22, 1, 6, -5, 3, 4]
print("List:",listA)
maxContiguousSubseqDP(listA)