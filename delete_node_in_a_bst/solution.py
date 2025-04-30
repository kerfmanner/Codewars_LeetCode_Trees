class Solution:
    def deleteNode(self, root, key: int):

        if not root:
            return None

        stack = []

        if root.val == key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            stack.append((None, root))

        else:
            parent = None
            ptr = root
            while ptr:
                if key < ptr.val:
                    parent, ptr = ptr, ptr.left
                elif key > ptr.val:
                    parent, ptr = ptr, ptr.right
                elif key == ptr.val:
                    stack.append((parent, ptr))
                    break

        while stack:
            parent, ptr = stack.pop()

            if not ptr.right:
                if parent.left == ptr: 
                    parent.left = ptr.left 
                else:
                    parent.right = ptr.left

            elif not ptr.left:
                if parent.left == ptr:
                    parent.left = ptr.right
                else:
                    parent.right = ptr.right
            else:
                successor = ptr.right
                parent = ptr
                while successor.left:
                    parent = successor
                    successor = successor.left

                ptr.val = successor.val

                stack.append((parent, successor))

        return root
