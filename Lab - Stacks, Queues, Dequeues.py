# Exercise 1 - Implement a Queue using 2 Stacks
#Stack - LIFO
#Queue - FIFO

# Class to Push an Element in a Stack
class PushStack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):  #Function to push/add the Element
        self.stack.append(element)   #Appends the element within the Stack
    
    def isEmpty(self):  #Function to check if the Stack is Empty
        return len(self.stack) == 0
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

#Class to Pop an Element in a Stack
class PopStack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):  #Function to pop/remove an Element
        if self.isEmpty():   #Checks if the Stack is Empty
            return None
        else:
            return self.stack.pop()  #If it's not, pops the Stack

#Queue Class using two stacks
class Queue:
    def __init__(self):
        self.push = PushStack()
        self.pop = PopStack()
    
    def enqueue(self, element):  #Add element to queue through Enqueue
        self.push.push(element)

    def dequeue(self):  #Remove element from queue through Dequeue
        if self.pop.isEmpty():
            while not self.push.isEmpty():
                self.pop.push(self.push.pop())
        return self.pop.pop()

#Sample Code
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) 
print(q.dequeue()) 
q.enqueue(4)
print(q.dequeue())  
print(q.dequeue())

#Exercise 2 - Given two queues with strings in ascending order, implement a function to move all the strings to,
#a third queue so that the third queue ends up with the strings in ascending order.
class Queue1_2:  #Queue Class for Queues 1 & 2
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):  #Function to enqueue elements
        self.queue.append(element)

    def dequeue(self):  #Function to dequeue elements
        if self.isEmpty():   #Checks if Queue is Empty
            return "Queue is empty"
        return self.queue.pop(0)   #Dequeues the first element

    def isEmpty(self):   #Function to check if the Queue is Empty
        return len(self.queue) == 0   


def Queue3(q1, q2):  #Function that merges both queues
    q3 = Queue1_2()
    while not q1.isEmpty() and not q2.isEmpty():  #While both queues have elements in them
        if q1.queue[0] <= q2.queue[0]:
            q3.enqueue(q1.dequeue())  
        else:
            q3.enqueue(q2.dequeue())

    #If any items left in q1
    while not q1.isEmpty():
        q3.enqueue(q1.dequeue())

    #If any items left in q2
    while not q2.isEmpty():
        q3.enqueue(q2.dequeue())

    return q3

#Sample Code
q1 = Queue1_2()
q2 = Queue1_2()

for s in ["apple", "banana"]:
    q1.enqueue(s)

for s in ["apricot", "blueberry"]:
    q2.enqueue(s)

q3 = Queue3(q1, q2)
print("Merged Queue:", q3.queue)

#Exercise 3 - Balanced Brackets Checker, check if a sequence of brackets (, {, [ is balanced.
class Stack:
    def __init__(self):
        self.stack = []  

    def isEmpty(self):  #Function to check if the Stack is Empty
        return len(self.stack) == 0

    def push(self, char):  #Function to push a character to the Stack
        self.stack.append(char)

    def pop(self):   #Function to pop a character to the Stack
        if self.isEmpty():  #Checks if the Stack is Empty
            return None
        return self.stack.pop()   #If it's not empty, pops the Stack

def is_balanced(characters):  #Function to check if characters are balanced
    stack = Stack()
    matching = {')': '(', '}': '{', ']': '['}  #Used a dictionary to ensure 

    for i in characters:
        if i in "({[":  #If it's a left bracket
            stack.push(i)
        elif i in ")}]":  #If it's a right bracket
            top = stack.pop()
            if top != matching[i]:  #Mismatched pair
                return "not balanced"

    #After processing all characters, stack must be empty
    if stack.isEmpty():
        return "balanced" 
    else:
        return "not balanced"

#Sample Tests
c1 = "{,[,],}"
c2 = "{,(,},)"
c3 = "(,{,),},)"

print(f"{c1} is {is_balanced(c1)}")  
print(f"{c2} is {is_balanced(c2)}")  
print(f"{c3} is {is_balanced(c3)}")