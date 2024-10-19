class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        if target < matrix[0][0] or target > matrix[-1][-1]:  #Check bounds
            return False
        
        n,m = len(matrix), len(matrix[0])
        
        # As both rows and cols are sorted. So we will eliminate both rows and cols
        # We will start from the last row and first col
        row, col = n-1, 0

        while row >= 0 and col < m:
            current = matrix[row][col]
            if current == target:
                return True
            elif current > target:
                # go 1 row back
                row -= 1
            else:
                col +=1
        
        return False

