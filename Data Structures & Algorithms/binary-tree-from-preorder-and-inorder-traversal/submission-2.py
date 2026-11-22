# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # O(1)
            root_index = inorder_map[root_val]
            
            left_size = root_index - in_start
            
            root.left = helper(pre_start + 1, pre_start + left_size, 
                               in_start, root_index - 1)
            
            root.right = helper(pre_start + left_size + 1, pre_end, 
                                root_index + 1, in_end)
            
            return root
        
        return helper(0, len(preorder)-1, 0, len(inorder)-1)