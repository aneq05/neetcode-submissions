# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# szukamy p i q w poddrzewach
# jeśli p w jednym i q w drugim to zwracamy root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None

        def dfs(root):
            if root is None:
                return None

            if root == p or root == q:
                return root

            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root
            
            return left if left else right

        lca = dfs(root)
        return lca

        
