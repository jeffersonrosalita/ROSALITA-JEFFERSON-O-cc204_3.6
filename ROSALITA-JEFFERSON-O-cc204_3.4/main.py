class TreeNode:
    """Represents a single node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder_dfs(node, result=None):
    """Depth-First Search (Preorder): Root -> Left -> Right."""
    if result is None:
        result = []
    if node is None:
        return result

    result.append(node.value)
    preorder_dfs(node.left, result)
    preorder_dfs(node.right, result)
    return result


def inorder_dfs(node, result=None):
    """Depth-First Search (Inorder): Left -> Root -> Right."""
    if result is None:
        result = []
    if node is None:
        return result

    inorder_dfs(node.left, result)
    result.append(node.value)
    inorder_dfs(node.right, result)
    return result


def postorder_dfs(node, result=None):
    """Depth-First Search (Postorder): Left -> Right -> Root."""
    if result is None:
        result = []
    if node is None:
        return result

    postorder_dfs(node.left, result)
    postorder_dfs(node.right, result)
    result.append(node.value)
    return result


def build_sample_tree():
    """
    Sample Tree:
          1
         / \
        2   3
       / \
      4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    return root


if __name__ == "__main__":
    tree_root = build_sample_tree()

    print("Preorder DFS (Root, Left, Right): ", preorder_dfs(tree_root))
    print("Inorder DFS  (Left, Root, Right): ", inorder_dfs(tree_root))
    print("Postorder DFS(Left, Right, Root): ", postorder_dfs(tree_root))