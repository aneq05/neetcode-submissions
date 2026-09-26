# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if node is None:
                return 0

            curr_is_good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)

            good_nodes_left = dfs(node.left, new_max)
            good_nodes_right = dfs(node.right, new_max)

            return(
                curr_is_good
                + good_nodes_left
                + good_nodes_right
            )

        return dfs(root, root.val)