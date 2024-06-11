# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool: # type: ignore
        #base case, if root = [], return False because empty tree
        if not root:
            return False
        #if no leaf on left and right, reached the end of tree. Compare sum of treeto targetSum
        if not root.left and not root.right:
            return targetSum - root.val == 0
        return (self.hasPathSum(root.left, targetSum - root.val)
            or self.hasPathSum(root.right, targetSum - root.val))
    
solution = Solution()
root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
targetSum = 22
result = solution.hasPathSum(root, targetSum)
print(result)