# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
    
def greatest_node(root: Node):
    node_max = root.value
    
    if root.left_child is not None:
        l_node_max = greatest_node(root.left_child)
    else:
        l_node_max = node_max

    if root.right_child is not None:
        r_node_max = greatest_node(root.right_child)
    else:
        r_node_max = node_max

    return max(node_max, l_node_max, r_node_max)
