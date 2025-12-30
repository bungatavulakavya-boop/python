class Node:
     def __init__(self,data):
         self.left=None
         self.data=data
         self.right=None
class Tree:
    def inorder(root):
        if root!=None:
            Tree.inorder(root.left)
            print(root.data,end=" ")
            Tree.inorder(root.right)
root=Node(10)
root.left=Node(20)
root.left.left=Node(40)
root.right=Node(30)
root.right.left=Node(50)
t=Tree()
Tree.inorder(root)
