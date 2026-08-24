class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue

    elif nodeValue <= rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftchild, nodeValue)

    else:
        if rootNode.rightchild is None:
            rootNode.rightchild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightchild, nodeValue)


def preOrderTraversal(rootNode):
    if not rootNode:
        return

    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return

    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data, end=" ")
    inOrderTraversal(rootNode.rightchild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return

    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data, end=" ")


# Create BST
bstObj = BSTNode(None)

insertNode(bstObj, 70)
insertNode(bstObj, 50)
insertNode(bstObj, 90)
insertNode(bstObj, 30)
insertNode(bstObj, 60)
insertNode(bstObj, 80)
insertNode(bstObj, 100)
insertNode(bstObj, 20)
insertNode(bstObj, 40)


# Traversals
print("Pre-order Traversal:")
preOrderTraversal(bstObj)

print("\nIn-order Traversal:")
inOrderTraversal(bstObj)

print("\nPost-order Traversal:")
postOrderTraversal(bstObj)