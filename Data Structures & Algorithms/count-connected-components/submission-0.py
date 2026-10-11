class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 1

        left = edges[0][1]

        for right in range(1, len(edges)):
            if left == edges[right][0]:
                left = edges[right][1]
            else:
                count += 1

        return count