class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def rob(self,root):
        def dfs(node):
            if not node:
                return (0,0)
            left=dfs(node.left)
            right=dfs(node.right)
            rob_this=node.val+left[1]+right[1]
            not_rob_this=max(left)+max(right)
            return (rob_this,not_rob_this)
        return max(dfs(root))
root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(3)
root.right.right=TreeNode(1)
s=Solution()
result=s.rob(root)
print("the maximum amount of money taken without alerting the police is:",result)    
    
            
            

        
        