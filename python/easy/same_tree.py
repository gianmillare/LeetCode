# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        # Begin the recursion here
        left_nodes_equal = self.isSameTree(p.left, q.left)
        right_nodes_equal = self.isSameTree(p.right, q.right)

        return left_nodes_equal and right_nodes_equal
