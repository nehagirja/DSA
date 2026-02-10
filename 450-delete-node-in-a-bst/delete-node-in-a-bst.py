# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key) 
        elif key > root.val: 
            root.right = self.deleteNode(root.right, key) 
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else: 
                minNode = self.minValue(root.right)
                root.val = minNode.val 
                root.right = self.deleteNode(root.right,minNode.val) #This time when you call it recursively it will be a simple case because it will not have a left child. 
        return root

    #Min value from the right subtree 
    def minValue(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr  #If there is no child, return parent. 