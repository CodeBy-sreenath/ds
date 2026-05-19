class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def bstval(self,root):
        def validate(node,low,high):
            if not node:
                return True
            if not low<node.val<high:
                return True
            left_validate=validate(node.left,low,node.val)
            right_validate=validate(node.right,node.val,high)
            return left_validate,right_validate
        return validate(root,float('-inf'),float('inf'))
root=TreeNode(2)
root.left=TreeNode(1)
root.right=TreeNode(3)
s=Solution()
print(s.bstval(root))    



