class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        transposed = zip(*matrix)

        for i, row in enumerate(transposed):
            matrix[i] = list(reversed(row))
