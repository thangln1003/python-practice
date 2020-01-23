

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printPreOrder(root: TreeNode):
    if root:
        print(root.val)
        printPreOrder(root.left)
        printPreOrder(root.right)


def printInOrder(root: TreeNode):
    if root:
        printInOrder(root.left)
        print(root.val)
        printInOrder(root.right)


def printPostOrder(root: TreeNode):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.val)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.rigt = TreeNode(5)

    print("\nPreOrder traversal of binary tree is")
    printPreOrder(root)

    print("\nInOrder traversal of binary tree is")
    printInOrder(root)

    print("\nPostOrder traversal of binary tree is")
    printPostOrder(root)
