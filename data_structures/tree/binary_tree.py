"""
Binary Tree
"""

class BinaryTreeNode:
    """ node of a tree. """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def traversal_preorder(self):
        """ root -> left -> right """
        print(str(self.data) + "->", end='')
        if self.left:
            self.left.traversal_preorder()
        if self.right:
            self.right.traversal_preorder()

    def traversal_inorder(self):
        """ left -> root -> right """
        if self.left:
            self.left.traversal_inorder()
        print(str(self.data) + "->", end='')
        if self.right:
            self.right.traversal_inorder()

    def traversal_postorder(self):
        """ left -> right -> root """
        if self.left:
            self.left.traversal_inorder()
        if self.right:
            self.right.traversal_inorder()
        print(str(self.data) + "->", end='')

tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)

print("\nPre-order traversal")
tree.traversal_preorder()
print("Inorder traversal\n")
tree.traversal_inorder()
print("Post-order traversal\n")
tree.traversal_postorder()
