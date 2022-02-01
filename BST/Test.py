import Tree

x = Tree.TreeNode(10)
print(x.is_empty())
print(x.preorder())


x.insert(1)
x.insert(2)
print(x.is_empty())
print(x.preorder())

print(x.find(2))

