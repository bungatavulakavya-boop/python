class Node:
     def __init__(self,data):
         self.left=None
         self.data=data
         self.right=None
class Tree:
    def postorder(root):
        if root!=None:
            Tree.postorder(root.left)
            Tree.postorder(root.right)
            print(root.data,end=" ")
root=Node(10)
root.left=Node(20)
root.left.left=Node(40)
root.right=Node(30)
root.right.left=Node(50)
t=Tree()
Tree.postorder(root)
