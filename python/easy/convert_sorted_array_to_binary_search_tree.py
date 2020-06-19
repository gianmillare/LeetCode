# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        middle = len(nums) // 2

        root_node = TreeNode(nums[middle])

        root_node.left = self.sortedArrayToBST(nums[:middle])
        root_node.right = self.sortedArrayToBST(nums[middle + 1:])

        return root_node
