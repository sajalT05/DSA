"""
Tree check
"""

class TreeNode:
    """ node of a tree. """
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def is_full_binary_tree(root):
    """ all nodes have 2 or no children """
    # empty case
    if root is None:
        pass

    # no child
    elif root.left is None and root.right is None:
        return True

    # have child --> Recursion check for left & right
    elif root.left is not None and root.right is not None:
        return is_full_binary_tree(root=root.left) and is_full_binary_tree(root=root.right)
    return False


def check_depth(root):
    """ check depth of a node. """
    depth_left = depth_right = 0
    check_root_left = check_root_right = root
    while check_root_left:
        depth_left += 1
        check_root_left = check_root_left.leaf
    while check_root_right:
        depth_right += 1
        check_root_right = check_root_right.right

    if depth_left == depth_right:
        return True

    return False


def is_perfect_binary_tree(root):
    """ all nodes have 2 children and all leaf at same level. """
    # empty case
    if root is None:
        pass

    # have child --> Recursion check for left & right
    elif root.left is not None and root.right is not None:
        return is_perfect_binary_tree(root=root.left) and is_perfect_binary_tree(root=root.right)

    return False


tree_root = TreeNode(1)
tree_root.left = TreeNode(2)
tree_root.right = TreeNode(3)
tree_root.left.left = TreeNode(4)
tree_root.left.right = TreeNode(5)
tree_root.right.left = TreeNode(6)
tree_root.right.right = TreeNode(7)

print(is_full_binary_tree(root=tree_root))
