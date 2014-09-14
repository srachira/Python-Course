__author__ = 'Kalyan'

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_tree(input):
    if input is None:
        return None

    if not isinstance(input, tuple):
        return TreeNode(input)

    assert len(input) == 3, "invalid input"
    root_val, left, right = input
    root = TreeNode(root_val)
    root.left = create_tree(left)
    root.right = create_tree(right)
    return root

def in_order(root, visit_func):
    if root is None:
        return
    in_order(root.left, visit_func)
    visit_func(root)
    in_order(root.right, visit_func)

def pre_order(root, visit_func):
    if root is None:
        return
    visit_func(root)
    pre_order(root.left, visit_func)
    pre_order(root.right, visit_func)

def post_order(root, visit_func):
    if root is None:
        return
    post_order(root.left, visit_func)
    post_order(root.right, visit_func)
    visit_func(root)


# sample visit functions - stateful and stateless.
def print_node(node):
    print node.value,

def count_nodes(node):
    global num_nodes
    num_nodes += 1

class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, node):
        self.count += 1


if __name__ == "__main__":
    input = (5, (10, 18, 20), 12)
    root = create_tree(input)
    print root