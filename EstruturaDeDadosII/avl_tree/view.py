from avl_tree import AVLTree
import random
avl = AVLTree()
root = None
nums = list(range(1, 10))

for num in nums:
    root = avl.insert(root, num)

print("Percurso em Largura (por nivel) depois da inserção -")
avl.percurso_nivel(root)
print()


key = nums[3]
root = avl.delete(root, key)
# pre_order Traversal
print("Percurso em Largura (por nivel) depois da remoção -")
avl.percurso_nivel(root)
print()
