def median(A, B):
    if len(A) > len(B):
        A, B = B, A

    start, end = 0, len(A)
    total_len = len(A) + len(B)

    while start <= end:
        midA = (start + end) // 2
        midB = (total_len + 1) // 2 - midA

        maxLeftA = float('-inf') if midA == 0 else A[midA - 1]
        minRightA = float('inf') if midA == len(A) else A[midA]

        maxLeftB = float('-inf') if midB == 0 else B[midB - 1]
        minRightB = float('inf') if midB == len(B) else B[midB]

        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            if total_len % 2 == 0:
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            else:
                return max(maxLeftA, maxLeftB)
        elif maxLeftA > minRightB:
            end = midA - 1
        else:
            start = midA + 1

print(median([1], [2]))  # return 1.5
print(median([1, 2], [3, 4]))  # returns 2.5
print(median([2, 3], [1, 4]))  # returns 2.5
print(median([1,3,5,7], [2,4,6,8]))  # returns 4.5
