"""
Tree traversal
"""

class TreeNode:
    """ node of a tree. """
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def preorder_traversal(root):
    """ root -> left node -> right node """

    if root: # if node exists
        # print root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder_traversal(root.left)
        # Traverse right
        preorder_traversal(root.right)

    return ''

def inorder_traversal(root):
    """ left node -> root -> right node """

    if root: # if node exists
        # Traverse left
        inorder_traversal(root.left)
        # print root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder_traversal(root.right)

    return ''

def postorder_traversal(root):
    """  left node -> right node -> root """

    if root: # if node exists
        # Traverse left
        postorder_traversal(root.left)
        # Traverse right
        postorder_traversal(root.right)
        # print root
        print(str(root.val) + "->", end='')

    return ''


tree_root = TreeNode(1)
tree_root.left = TreeNode(2)
tree_root.right = TreeNode(3)
tree_root.left.left = TreeNode(4)
tree_root.left.right = TreeNode(5)
tree_root.right.left = TreeNode(6)
tree_root.right.right = TreeNode(7)

print("Pre-order traversal")
print(f"{preorder_traversal(root=tree_root)}")
print("Inorder traversal ")
print(f"{inorder_traversal(root=tree_root)}")
print("Post-order traversal")
print(f"{postorder_traversal(root=tree_root)}")
