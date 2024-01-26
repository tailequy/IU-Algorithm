#Maximum Contiguous Subarray Problem
#given a sequence A of n integers A[1 . . n]
# we need to find the largest sum possible in a contiguous subsequence A[i . . j] of A
#Eg: A = [−6, − 22, 1, 6, −5, 3, 4]
# The maximum contiguous subsequence is [1, 6, − 5, 3, 4] with a sum of 9
#Brute-force algorithm: simply be to compute the subarray sum for each possible pair i, j
# satisfying 0 ≤ i ≤ j ≤ n − 1 and keep track of the maximum
# Complexity: O(n^3)
def maxContiguousSubseq(A):
    maxSum = 0
    n = len(A)
    for i in range(0,n):
        for j in range(i,n):
            subseqSum = 0
            for k in range(i,j+1):
                subseqSum += A[k]
                maxSum=max(maxSum, subseqSum)
    print("maxSum =", maxSum)

#Input an array
n = int(input("Input a number: "))
A = []
for i in range(n):
    A.append(int(input("Input a number: ")))
#Compute the maxsum
maxContiguousSubseq(A)