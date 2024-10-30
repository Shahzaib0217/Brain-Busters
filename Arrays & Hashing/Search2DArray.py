class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        # Create 3 pointers left, mid, right
        left = 0
        # Flatten the 2D array into 1D Array (as right should be the last index of last row)
        right = rows * cols - 1

        while left <= right:
            # Create logic to traveerse the array
            mid = (left + right) // 2

            mid_value=matrix[mid//cols][mid%cols]

            # Compare the target with mid value 
            if mid_value == target:
                #  return true if equal to mid value
                return True

            if mid_value > target: 
                right = mid -1
            
            if mid_value < target:
                left = mid + 1

        return False


        
