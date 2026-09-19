class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_row = 0
        last_row = len(matrix) - 1

        # row search
        while first_row <= last_row:
            mid = (first_row+last_row)//2

            if target > matrix[mid][-1]:
                first_row = mid + 1
            elif target < matrix[mid][0]:
                last_row = mid - 1
            else:
                break
        
        # element search in row
        row_vals = matrix[mid]
        left, right = 0, len(row_vals)-1

        while left <= right:
            middle = (left+right)//2

            if row_vals[middle] == target:
                return True
            elif row_vals[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False



            

