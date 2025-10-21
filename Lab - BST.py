#Exercise 1: Exercise-1: 
#Insert a new student with unique PSU ID and student details using BST. 
#Find a student using PSU ID. 
#Print each student with all details.

#Class for Binary Tree
class Tree:
    def __init__(self, id, details):
        self.id = id
        self.details = details
        self.right = None
        self.left = None

#Function to insert a new Student in BST
def insert(root, id, details):
    if root is None:
        return Tree(id, details)
    if id == root.id:
        print("No Duplicates")
        return root
    elif id < root.id:
        root.left = insert(root.left, id, details)
    else:
        root.right = insert(root.right, id, details)
    return root

#Function to search by ID
def search(root, id):
    if root is None:
        return None
    if root.id == id:
        return root
    elif id < root.id:
        return search(root.left, id)
    else:
        return search(root.right, id)

#Print all Students Details
def printInorder(root):
    if root:
        printInorder(root.left)
        print(f"PSU ID: {root.id}. Name: {root.details['name']}, Major: {root.details['major']}")
        printInorder(root.right)

#Testing out my Code
if __name__ == "__main__":
    #initial Tree
    root = None
    root = insert(root, "123456789", {"name": "Wilson Quilli", "major": "CS"})
    root = insert(root, "012345678", {"name": "Faahil Amer", "major": "CS"})

    print("Current Tree: ")
    printInorder(root)

    #Insertion Function 
    root = insert(root, "001234567", {"name": "Nick S.", "major": "CS"})

    print("\nAll Students: ")
    printInorder(root)  #New Tree with new addition

    #Search Function
    search_student = "123456789"
    found = search(root, search_student)
    if found:
        print(f"\nStudent Found: PSU ID {found.id}, Name: {found.details['name']}")
    else:
        print(f"\nStudent with ID {search_student} not found.")