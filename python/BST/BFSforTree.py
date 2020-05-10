""" BFS Binary Tree

        1
      /   \
     2     3
   /   \
  4     5

*Breadth First Traversal:
    LevelOrder Traversal  : 1 2 3 4 5"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode):
    if root:
        print(root.val, end=" ")


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Level Order: ", end=" ")
    levelOrder(root)
