class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i, row in enumerate(matrix):
        #     for j, col in enumerate(row):
        #         if
        for row in matrix:
            for col in row:
                if col == target:
                    return True
        return False 

