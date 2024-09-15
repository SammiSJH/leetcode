# 2024-09-15
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        dq = deque()
        dq.append(root)
        res = []

        while dq:

            snap = len(dq)
            for i in range(snap):

                node = dq.popleft()

                if i == snap - 1:
                    res.append(node.val)

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)

        return res
