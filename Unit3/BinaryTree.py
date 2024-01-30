#Traversing and linearization of trees
#Binary tree
aTree=['A', #Root
    ['B', #Left Subtree
    ['D',[],[]],
    []],
    ['C', #Right Subtree
    ['E',
    ['G',[],[]],
    []],
    ['F',[],[]]
    ]]
def treeRoot(aTree):
    if(aTree):
        return aTree[0]
def leftSubTree(aTree):
    if(aTree):
        return aTree[1]
def rightSubTree(aTree):
    if(aTree):
        return aTree[2]
#We can print the root, left subtree, and right subtree
print(treeRoot(aTree))
print(leftSubTree(aTree))
print(rightSubTree(aTree))

#In-order Traversal
#we recursively perform an in-order traversal of the left subtree, root node, right subtree

def inorder(aTree):
    if aTree:
        inorder(leftSubTree(aTree))
        print(treeRoot(aTree))
        inorder(rightSubTree(aTree))

#Preorder Traversal
#we visit the root node, followed by recursive preorder traversals left subtrees, right subtrees

def preorder(aTree):
    if aTree:
        print(treeRoot(aTree))
        preorder(leftSubTree(aTree))
        preorder(rightSubTree(aTree))

#Postorder Traversal
#we recursively perform an postorder traversal of the left subtree, right subtree, root node.
def postorder(aTree):
    if aTree:
        postorder(leftSubTree(aTree))
        postorder(rightSubTree(aTree))
        print(treeRoot(aTree))

print("In-order traversal")
inorder(aTree)
print("Preorder traversal")
preorder(aTree)
print("Postorder travesal")
postorder(aTree)

