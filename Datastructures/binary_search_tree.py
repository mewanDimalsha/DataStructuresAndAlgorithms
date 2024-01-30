#creation of Binary search Tree
class BST_node:
    def __init__(self,data) -> None:
        self.data=data
        self.leftChild = None
        self.rightChild = None

#inserting operation
def insert_node(root_node,node_value):
    if root_node.data==None :
        root_node.data = node_value
        
    

newBST = BST_node(None)
print(newBST.data)  