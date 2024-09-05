"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return 'Node(' + repr(self.val) + ', ' + repr(self.left) + ', ' + repr(self.right) + ")"\
            
tree = Node('root', Node('left', Node('left.left')), Node('right'))
serialized_tree = repr(tree)
deserialized_tree = eval(serialized_tree)
assert deserialized_tree.left.left.val == 'left.left'
    

# eval() function parse the expression argument and evaluate it as a Python expression and runs Python expression (code) within the program.
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.