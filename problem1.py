from collections import deque


class Node:
    """A single node of a binary tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    """Build the binary tree for Problem 1."""
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


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)


def preorder(node):
    if node is None:
        return []
    return [node.data] + preorder(node.left) + preorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.data]


def level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


if __name__ == "__main__":
    tree_root = build_tree()
    print("Inorder:", " ".join(map(str, inorder(tree_root))))
    print("Preorder:", " ".join(map(str, preorder(tree_root))))
    print("Postorder:", " ".join(map(str, postorder(tree_root))))
    print("Level-order:", " ".join(map(str, level_order(tree_root))))