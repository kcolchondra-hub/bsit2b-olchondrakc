from collections import deque


class Node:
    """A single node of a binary tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    """Build the binary tree from Problem 1."""
    root = Node(15)
    root.left = Node(10)
    root.right = Node(25)

    root.left.left = Node(4)
    root.left.right = Node(12)
    root.right.left = Node(20)
    root.right.right = Node(30)

    root.left.left.left = Node(2)
    root.left.left.right = Node(6)
    return root


def size(node):
    """Number of nodes in the tree rooted at node."""
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)


def height(node):
    """Height in EDGES; empty tree -> -1, single node -> 0."""
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def iterative_size(root):
    """Compute the number of nodes iteratively using level-order traversal."""
    if root is None:
        return 0
    count = 0
    queue = deque([root])
    while queue:
        current = queue.popleft()
        count += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return count


if __name__ == "__main__":
    tree_root = build_tree()
    print("Recursive size:", size(tree_root))
    print("Iterative size:", iterative_size(tree_root))
    print("Height (edges):", height(tree_root))