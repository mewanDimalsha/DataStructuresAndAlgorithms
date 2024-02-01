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
    elif node_value <= root_node.data :
        if root_node.leftChild is None:
            root_node.leftChild = BST_node(node_value)
        else:
            insert_node(root_node.leftChild,node_value)
    else:
        if root_node.rightChild is None:
            root_node.rightChild = BST_node(node_value)
        else:
            insert_node(root_node.rightChild,node_value)
    return "node inserted."

def preOrderTraversal(rootnode):
    if rootnode.data is None:
        return
    print(rootnode.data)
    preOrderTraversal(rootnode.leftChild)
    preOrderTraversal(rootnode.rightChild)

def inOrderTraversal(rootnode):
    if rootnode.data is None:
        return
    inOrderTraversal(rootnode.leftChild)
    print(rootnode.data)
    inOrderTraversal(rootnode.rightChild)

def postOrderTraversal(rootnode):
    if rootnode.data is None:
        return
    postOrderTraversal(rootnode.leftChild)
    postOrderTraversal(rootnode.rightChild)
    print(rootnode.data)
    
def searchNode(rootnode,node_value):
    if rootnode.data == node_value:
        print("found")
    elif node_value < rootnode.data:
        if rootnode.leftChild is not None:
            if rootnode.leftChild.data == node_value:
                print("found")
            else :
                searchNode(rootnode.leftChild,node_value)
        else:
            print("not found")
    else:
        if rootnode.rightChild is not None:
            if rootnode.rightChild.data == node_value:
                print("found")
            else :
                searchNode(rootnode.rightChild,node_value)
        else:
            print("not found")
  
def minValNode(bstNode):
    current = bstNode
    while(current.leftChild is not None):
        current = current.leftChild
    return current
              
def deleteNode(rootNode,node_value):
    if rootNode is None:
        return rootNode
    if node_value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,node_value)
    elif node_value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,node_value)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode=None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        else:
            temp = minValNode(rootNode.rightChild)
            rootNode.data = temp.data
            rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
    return rootNode
            
newBST = BST_node(10)
print(insert_node(newBST,9))
print(newBST.leftChild.data)  