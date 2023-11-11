
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self) -> None:
        pass

    def invertTree(self, root: Optional[TreeNode]):
        if not root:
            return None
        root.left,root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], left+right+2)
            return 1+max(left, right)
        return res[0]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            return [balanced, 1+max(left[1], right[1])]
        return dfs(root)[0]

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        if q.val == p.val:
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)

    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:
            return True
        if not s:
            return False
        if t and s and self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])
        q.append(root)
        while q:
            qlen = len(q)
            rightNode = None
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightNode = node
                    q.append(node.left)
                    q.append(node.right)
            if rightNode:
                res.append(rightNode.val)
        return res

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxValue):
            if not root:
                return 0
            res = 1 if root.val > maxValue else 0
            maxValue = max(maxValue, root.val)
            res += dfs(root.left, maxValue)
            res += dfs(root.right, maxValue)
            return res
        return dfs(root, root.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValied(root, left, right):
            if not root:
                return True
            if not (root.val > left and root.val < right):
                return False
            return isValied(root.left, left, root.val) and isValied(root.right, root.val, right)
        return isValied(root, float("-inf"), float("inf"))

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n+=1
            if n==k:
                return cur.val
            cur = cur.right

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root


if __name__ == "__main__":
    _root = TreeNode()
    _root.val = 1

    left = TreeNode()
    left.val = 2

    right = TreeNode()
    right.val = 3

    _root.left = left
    _root.right = right

    tp = Tree()
    tp.rightSideView(_root)
