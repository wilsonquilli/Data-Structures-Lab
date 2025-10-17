#Exercise 1
#Class for the Node in my Binary Search Tree
class Node:
    def __init__(self, key):
        self.left = None #Left child
        self.right = None #Right child
        self.val = key #Node value

#Function to insert a node to a tree
def insert(root, key):
    if root is None: #If the tree is empty
        return Node(key) #Create a new node
    else:
        if root.val < key: #If the key is greater than the root value
            root.right = insert(root.right, key) #Insert to the right subtree
        else:
            root.left = insert(root.left, key) #Insert to the left subtree
    return root  #In the end, return the root

#Function to perform In-order traversal
def inorder_traversal(root):
    if root: #If the root is not None
        inorder_traversal(root.left) #Traverse the left subtree
        print(root.val, end=' ') #Print the root value
        inorder_traversal(root.right) #Traverse the right subtree

#Function to perform Pre-order traversal
def preorder_traversal(root):
    if root: #If the root is not None
        print(root.val, end=' ') #Print the root value
        preorder_traversal(root.left) #Traverse the left subtree
        preorder_traversal(root.right) #Traverse the right subtree

#Function to perform Post-order traversal
def postorder_traversal(root): 
    if root: #If the root is not None
        postorder_traversal(root.left) #Traverse the left subtree
        postorder_traversal(root.right) #Traverse the right subtree
        print(root.val, end=' ') #Print the root value

#Function to find a node in the tree
def search(root, key):
    if root is None or root.val == key: #Checks if the root is None or the key is the root value
        return root #Return the node if found or None if not found
    if root.val < key: #If the key is greater than the root value
        return search(root.right, key) #Search in the right subtree
    return search(root.left, key) #Else, search in the left subtree

#Function to find the minimum value in the tree
def min_value(root):
    if root is None: #If the tree is empty
        return -1 #Return -1 for empty tree
    curr = root #Start from the root
    while curr.left is not None: #Go to the leftmost node
        curr = curr.left #Update current node
    return curr.val #Return the minimum value

#Function to find the maximum value in the tree
def max_value(root):
    if root is None: #If the tree is empty
        return -1 #Return -1 for empty tree
    curr = root #Start from the root
    while curr.right is not None: #Go to the rightmost node
        curr = curr.right #Update current node
    return curr.val #Return the maximum value

#Exercise 2
def successor(node):
    current = node.right #Start from the right child
    while current.left is not None: #Go to the leftmost node
        current = current.left #Update current node
    return current #Return the successor node

#Function to remove a node from the tree
def delete_node(root, key):
    if root is None: #If the tree is empty
        return root #Return None
    if key < root.val: #If the key is less than the root value
        root.left = delete_node(root.left, key) #Go to the left subtree
    elif key > root.val: #If the key is greater than the root value
        root.right = delete_node(root.right, key) #Go to the right subtree
    else: #If the key is found
        if root.left is None: #Case 1 and Case 2: Node with only one child or no child
            return root.right #Return the right child
        elif root.right is None: #Case 1 and Case 2: Node with only one child or no child
            return root.left #Return the left child
        temp = successor(root) #Case 3: Node with two children, get the inorder successor (smallest in the right subtree)
        root.val = temp.val #Copy the inorder successor's content to this node
        root.right = delete_node(root.right, temp.val) #Delete the inorder successor
    return root #Return the (possibly updated) root

#Exercise 3
def merge_trees(t1, t2):
    if not t1: #If the first tree is None
        return t2 #Return the second tree
    if not t2: #If the second tree is None
        return t1 #Return the first tree
    t1.val += t2.val #Merge the values of the two nodes
    t1.left = merge_trees(t1.left, t2.left) #Merge the left subtrees
    t1.right = merge_trees(t1.right, t2.right) #Merge the right subtrees
    return t1 #Return the merged tree

#Exercise 4
def conversion(arr):
    if not arr: #If the array is empty
        return None #Return None
    mid = len(arr) // 2 #Find the middle index
    root = Node(arr[mid]) #Create a node with the middle element
    root.left = conversion(arr[:mid]) #Recursively build the left subtree
    root.right = conversion(arr[mid+1:]) #Recursively build the right subtree
    return root #Return the root of the BST

def bst_checker(root, low=float('-inf'), high=float('inf')):
    if root is None: #If the tree is empty
        return True #An empty tree is a valid BST
    if not (low < root.val < high): #Check the current node value against the allowed range
        return False #If it violates the BST property, return False
    return (bst_checker(root.left, low, root.val) and #Recursively check the left subtree
            bst_checker(root.right, root.val, high)) #Recursively check the right subtree

if __name__ == "__main__":
    values = [50, 30, 20, 40, 70, 60, 80, 10, 35, 65] #Create a tree with at least 10 values
    root = None
    for val in values:
        root = insert(root, val)

    print("In-order Traversal:")
    inorder_traversal(root)
    print("\n")

    print("Pre-order Traversal:")
    preorder_traversal(root)
    print("\n")

    print("Post-order Traversal:")
    postorder_traversal(root)
    print("\n")

    #Search for nodes
    print("Search for 40:", "Found" if search(root, 40) else "Not Found")
    print("Search for 100:", "Found" if search(root, 100) else "Not Found")
    print()

    #Minimum and Maximum
    print("Minimum value in the tree:", min_value(root))
    print("Maximum value in the tree:", max_value(root))
    print()

    #Delete nodes (leaf, one child, two children)
    print("Deleting a leaf node (10)...")
    root = delete_node(root, 10)
    inorder_traversal(root)
    print("\n")

    print("Deleting a node with one child (30)...")
    root = delete_node(root, 30)
    inorder_traversal(root)
    print("\n")

    print("Deleting a node with two children (50)...")
    root = delete_node(root, 50)
    inorder_traversal(root)
    print("\n")

    #Merge trees
    t1 = None
    for val in [1, 3, 5]:
        t1 = insert(t1, val)
    t2 = None
    for val in [2, 4, 6]:
        t2 = insert(t2, val)
    merged = merge_trees(t1, t2)
    print("In-order traversal of merged tree:")
    inorder_traversal(merged)
    print("\n")

    #Conversion from sorted list
    print("Building BST from sorted list [1,2,3,4,5,6,7,8,9,10]:")
    arr_tree = conversion([1,2,3,4,5,6,7,8,9,10])
    inorder_traversal(arr_tree)
    print("\n")

    #Check if valid BST
    print("Is arr_tree a valid BST?", bst_checker(arr_tree))