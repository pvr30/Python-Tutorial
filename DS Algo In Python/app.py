from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(13))

print(tree.head)
print(tree.head.left)
print(tree.head.right)
print(tree.find(13))
print(tree.find(11))