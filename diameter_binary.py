class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def diameter_binary(self,root):
        self.diameters=0
        def dfs(node):
            if not node:
                return 0
            left_height=dfs(node.left)
            right_height=dfs(node.right)
            self.diameters=max(self.diameters,left_height+right_height)
            return 1+max(left_height,right_height)
        dfs(root)
        return self.diameters
               
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
s=Solution()
print(s.diameter_binary(root))        