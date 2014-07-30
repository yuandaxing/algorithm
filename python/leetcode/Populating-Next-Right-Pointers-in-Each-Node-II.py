class Solution:
        def nextParent(self, root) :
            while root and not root.left and not root.right :
                root = root.next 
            if not root : return None
            return root.left if root.left else root.right
        def connect(self, root):
            temp = TreeNode(0)
            while root :
                parent, prev = root, temp
                while parent :
                    if parent.left :
                        prev.next, prev = parent.left, parent.left
                    if parent.right :
                        prev.next, prev = parent.right, parent.right
                    parent = parent.next
                root = self.nextParent(root)
