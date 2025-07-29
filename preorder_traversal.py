# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]
        """
        if not root:
            return []
        output, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return output