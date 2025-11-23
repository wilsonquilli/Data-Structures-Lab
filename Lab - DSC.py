import time
import random

#Function to read my dataset
def load_employees(filename):
    employees = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data_start = None
    for i, line in enumerate(lines):
        if line.strip().upper().startswith("@DATA"):
            data_start = i + 1
            break

    headers = [
        "Employee_ID", "Age", "Salary", "Gender", "Department", "Experience",
        "Education", "Performance_Score", "Working_Hours", "City", "Country",
        "Years_in_Company", "Previous_Company", "Annual_Bonus",
        "Join_Date", "Name"
    ]

    for line in lines[data_start:]:
        s = line.strip()
        if not s or s.startswith("%"):
            continue
        parts = [p.strip() for p in s.replace("'", "").replace('"', "").split(",")]
        if len(parts) != len(headers):
            continue

        emp = {k: v for k, v in zip(headers, parts)}
        try:
            emp["employee_id"] = int(emp.pop("Employee_ID"))
        except:
            continue

        employees.append(emp)

    return employees

#Linked List Class
class LLNode:
    def __init__(self, emp):
        self.data = emp
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, emp): #Function to append to the Linked List
        new = LLNode(emp)
        if self.head is None:
            self.head = new
            self.last = new
        else:
            self.last.next = new
            self.last = new

    def delete(self, emp_id):  #Function to delete from linked list
        curr = self.head
        prev = None

        while curr:
            if curr.data["employee_id"] == emp_id:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                if curr is self.last:
                    self.last = prev
                return
            prev = curr
            curr = curr.next

#Binary Search Tree class
class BSTNode:
    def __init__(self, emp_id, details):
        self.emp_id = emp_id
        self.details = details
        self.left = None
        self.right = None

def bst_insert(root, emp_id, details):  #Function to insert into BST
    if root is None:
        return BSTNode(emp_id, details)
    curr = root
    while True:
        if emp_id < curr.emp_id:
            if curr.left is None:
                curr.left = BSTNode(emp_id, details)
                return root
            curr = curr.left
        elif emp_id > curr.emp_id:
            if curr.right is None:
                curr.right = BSTNode(emp_id, details)
                return root
            curr = curr.right
        else:
            return root

def bst_delete(root, emp_id):  #Function to delete from BST
    if root is None:
        return None
    if emp_id < root.emp_id:
        root.left = bst_delete(root.left, emp_id)
    elif emp_id > root.emp_id:
        root.right = bst_delete(root.right, emp_id)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        succ = root.right
        while succ.left:
            succ = succ.left
        root.emp_id = succ.emp_id
        root.details = succ.details
        root.right = bst_delete(root.right, succ.emp_id)
    return root

def build_bst(employees):  #Builds my BST
    shuffled = employees[:]
    random.shuffle(shuffled)
    root = None
    for emp in shuffled:
        root = bst_insert(root, emp["employee_id"], emp)
    return root

#Function to Print all values (List)
def time_print_list(lst):
    start = time.process_time()
    for _ in lst:
        pass
    print(f"LIST PRINT   → {round(time.process_time() - start, 6)} sec")

#Function to Print all values (Dictionary)
def time_print_dict(d):
    start = time.process_time()
    for _ in d.values():
        pass
    print(f"DICT PRINT   → {round(time.process_time() - start, 6)} sec")

#Function to Print all values (Linked List)
def time_print_ll(ll):
    curr = ll.head
    start = time.process_time()
    while curr:
        curr = curr.next
    print(f"LL PRINT     → {round(time.process_time() - start, 6)} sec")

#Function to Print all values (BST)
def time_print_bst(root):
    stack = []
    curr = root
    start = time.process_time()
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        curr = curr.right
    print(f"BST PRINT    → {round(time.process_time() - start, 6)} sec")

#Function to retrieve values (List)
def time_retrievals_list(lst, ids):
    print("\nList Retrievals: ")
    for t in ids:
        start = time.process_time()
        for emp in lst:
            if emp["employee_id"] == t: break
        print(t, "→", round(time.process_time() - start, 6))

#Function to retrieve values (Dictionary)
def time_retrievals_dict(d, ids):
    print("\nDICT RETRIEVALS: ")
    for t in ids:
        start = time.process_time()
        _ = d.get(t)
        print(t, "→", round(time.process_time() - start, 6))

#Function to retrieve values (Linked List)
def time_retrievals_linked_list(ll, ids):
    print("\nLinked List Retrievals: ")
    for t in ids:
        curr = ll.head
        start = time.process_time()
        while curr and curr.data["employee_id"] != t:
            curr = curr.next
        print(t, "→", round(time.process_time() - start, 6))

#Function to retrieve values (BST)
def time_retrievals_bst(root, ids):
    print("\nBST Retrievals: ")
    for t in ids:
        curr = root
        start = time.process_time()
        while curr:
            if curr.emp_id == t: break
            curr = curr.left if t < curr.emp_id else curr.right
        print(t, "→", round(time.process_time() - start, 6))

#Function for Insertions for all data structures
def time_insertions(lst, d, ll, bst_root):
    print("\nInsertion Times")
    next_id = max(e["employee_id"] for e in lst) + 10
    for run in range(1, 6):
        new_emp = {"employee_id": next_id, "Name": f"TestUser{run}"}
        
        start = time.process_time()
        lst.append(new_emp)
        print("LIST →", round(time.process_time() - start, 6))
        
        start = time.process_time()
        d[next_id] = new_emp
        print("DICT →", round(time.process_time() - start, 6))

        start = time.process_time()
        ll.append(new_emp)
        print("LL   →", round(time.process_time() - start, 6))

        start = time.process_time()
        bst_insert(bst_root, next_id, new_emp)
        print("BST  →", round(time.process_time() - start, 6))

        next_id += 10

#Function for Deletions for all data structures
def time_deletions(lst, d, ll, bst_root):
    print("\nDeletion Times: ")
    ids = random.sample([e["employee_id"] for e in lst], 5)
    print("Deleting:", ids)
    for target in ids:

        start = time.process_time()
        for i, e in enumerate(lst):
            if e["employee_id"] == target: lst.pop(i); break
        print("LIST →", round(time.process_time() - start, 6))

        start = time.process_time()
        d.pop(target, None)
        print("DICT →", round(time.process_time() - start, 6))

        start = time.process_time()
        ll.delete(target)
        print("LL   →", round(time.process_time() - start, 6))

        start = time.process_time()
        bst_delete(bst_root, target)
        print("BST  →", round(time.process_time() - start, 6))

def main():
    employees = load_employees("dataset.csv")

    lst = employees[:]
    d = {e["employee_id"]: e for e in employees}
    ll = LinkedList()
    for e in employees: ll.append(e)
    bst_root = build_bst(employees)

    print("\nPrinting all Values: ")
    time_print_list(lst)
    time_print_dict(d)
    time_print_ll(ll)
    time_print_bst(bst_root)

    print("\nRetrieving a Value: ")
    ids = random.sample([e["employee_id"] for e in employees], 5)
    time_retrievals_list(lst, ids)
    print("\n")
    time_retrievals_dict(d, ids)
    print("\n")
    time_retrievals_linked_list(ll, ids)
    print("\n")
    time_retrievals_bst(bst_root, ids)

    print("\nInsertions: ")
    time_insertions(lst, d, ll, bst_root)
    print("\n")

    print("\nDeletions: ")
    time_deletions(lst, d, ll, bst_root)
    print("\n")

if __name__ == "__main__":
    main()