class Node:
     def __init__(self,data):
         self.left=None
         self.data=data
         self.right=None
class Tree:
    def preorder(root):
        if root!=None:
            print(root.data,end=" ")
            Tree.preorder(root.left)
            Tree.preorder(root.right)
root=Node(10)
root.left=Node(20)
root.left.left=Node(40)
root.right=Node(30)
root.right.left=Node(50)
t=Tree()
Tree.preorder(root)
