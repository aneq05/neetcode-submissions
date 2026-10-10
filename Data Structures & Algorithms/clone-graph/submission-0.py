"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = []
        if node is None:
            return []
        if node.neighbours is None:
            return [[]]
# [[2],[1,3],[2]]
# 1 -> 2
# 2 -> 1 , 3
# 3 -> 2
# 1-indexed

        return graph