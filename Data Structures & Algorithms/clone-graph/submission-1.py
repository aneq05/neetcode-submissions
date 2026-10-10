"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        visited = {}

        def dfs(curr):
            if curr in visited:
                return visited[curr]

            copy = Node(curr.val)
            visited[curr] = copy

            for neighbor in curr.neighbors:
                copied_neigh = dfs(neighbor)
                copy.neighbors.append(copied_neigh)

            return copy

        return dfs(node)
# [[2],[1,3],[2]]
# 1 -> 2
# 2 -> 1 , 3
# 3 -> 2
# 1-indexed
