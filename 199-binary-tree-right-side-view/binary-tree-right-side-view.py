# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        queue = collections.deque()
        queue.append(root)

        if not root:
            return output
        
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(level[-1])
        return output 

# The space complexity of this BFS level order traversal is O(n) because in the worst case the queue can store up to half of the nodes in the tree at once (such as the last level of a complete binary tree), which is proportional to n. Although the level list is recreated for each level, at any moment it can hold up to the number of nodes in the largest level, which is also O(n) in the worst case. The output list stores one value per level, which could be O(n) in a skewed tree. Since we consider the maximum space used at any time, the overall space complexity is O(n).
