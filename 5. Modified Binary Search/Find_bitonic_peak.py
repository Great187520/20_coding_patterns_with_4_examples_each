class Solution:
    def find_highest_number(A):
        low = 0
        high = len(A) - 1

        #Require at least 3 elements for a valid bitonic sequence
        if len(A) < 3:
            return None
        
        while low <= high:
            mid = (low + high) // 2

            mid_left = A[mid - 1] if mid - 1 > 0 else float("-inf")
            mid_right = A[mid + 1] if mid + 1 < len(A) else float("inf")

            if mid_left < A[mid] and mid_right > A[mid]:
                low = mid + 1
            elif mid_left > A[mid] and mid_right < A[mid]:
                high = mid - 1

            elif mid_left < A[mid] and mid_right < A[mid]:
                return A[mid]