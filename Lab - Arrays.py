#My vector class
class Vector:
    def __init__(self):  
        self.capacity = 2  #Initial Capacity of 2
        self.size = 0   #Current number of elements
        self.items = [None] * self.capacity  #Creates an Array with initial capacity

    def length(self):  #Function that returns the number of elements in the vector
        return self.size
    
    def contains(self, item):  #Function that checks if the item is in the vector
        for i in range(self.size):  #Loops through the Vector size
            if self.items[i] == item:  #Checks for that item
                return True  #If it's found, returns True
        return False  #If it's not found, returns False
    
    def getItem(self, index):  #Function that returns the item stored in the index of the vector
        if 0 <= index < self.size:  #If the index is greater/equal than 0 and less than the Vector size,
            return self.items[index]   #Returns the element at the index
        else:
            raise IndexError("Index out of range.")  #Raises Error to indicate the index is out of range

    def setItem(self, index, item):  #Function that sets the value at the specified index
        if 0 <= index <= self.size:  #If the index is greater/equal than 0 and less than the Vector size,
            self.items[index] = item  #Sets the elemnt at the index
        else:
            raise IndexError("Index out of Range")  #Raises Error to indicate the index is out of range

    def resize(self):  #Function tha doubles the capacity of the array
        self.capacity *= 2  #Doubles the capacity
        new_items = [None] * self.capacity  #Creates a new larger array
        for i in range(self.size):
            new_items[i] = self.items[i]  #Copies existing elements to the new array
        self.items = new_items  #Replaces the old array with the new array

    def addItem(self, item):  #Function that adds a value to the Vector
        if self.size >= self.capacity:  #Checks that the size is smaller/equal than the capacity
            self.resize()  #Resizes the array if needed
        self.items[self.size] = item    #Adds item to the end
        self.size += 1  #Adds 1 to the total size

    def insertItem(self, index, item):  #Function that inserts a value in the index position
        if not (0 <= index <= self.size):  #Checks the index
            raise IndexError("Index out of Range")
        if self.size >= self.capacity:
            self.resize()  #Calls the resize function if full
        for i in range(self.size, index, -1):  #Shifts the elements to the right
            self.items[i] = self.items[i - 1]
        self.items[index] = item  #Inserts the new item
        self.size += 1
    
    def removeItem(self, index):  #Function that removes and returns the item from the element from the given index position
        if not (0 <= index < self.size):
            raise IndexError("Index out of range.")
        removed_item = self.items[index]  #Stores the item to return
        for i in range(index, self.size - 1):   #Shift elements to the left
            self.items[i] = self.items[i + 1]
        self.items[self.size - 1] = None  #Clears last element
        self.size -= 1  #Decreaes the size of the array by 1
        return removed_item  #Returns the removed item
    
    def indexOfItem(self, item):  #Function that returns the index of the vector element containing the given item
        for i in range(self.size):  #Loop through Vector length
            if self.items[i] == item:  #Checks for the specified item
                return i  #Returns the item
        raise ValueError(f"{item} not found in the Vector")  #If not found, this f-string will print

    def extend(self, otherVector):  #Function that extends this vector by appending another vector
        for i in range(otherVector.length()):  #Loops through the Other Vector
            self.addItem(otherVector.getItem(i))  #Appends each item to current vector

    def subVector(self, start, end):  #Function that creates and returns a new vector that contains a subsequence of the items
        if not (0 <= start <= end < self.size):
            raise IndexError("Indices out of range.")
        new_vector = Vector()  #Creates new Vector
        for i in range(start, end + 1):  #Loops through the subsequence
            new_vector.addItem(self.items[i])  #Adds item to the new Vector
        return new_vector  #Returns the new Vector

#Sample Code
v = Vector()
v.addItem(1)
v.addItem(2)
v.addItem(3)

print("Length:", v.length()) 
print("Contains 2?", v.contains(2))  
print("Item at index 1:", v.getItem(1))  
v.setItem(1, 4)
print("Item at index 1 after set:", v.getItem(1)) 
v.insertItem(1, 5)
print("Items after insert at index 1:", [v.getItem(i) for i in range(v.length())]) 
removed = v.removeItem(2)
print("Removed item:", removed) 
print("Items after remove:", [v.getItem(i) for i in range(v.length())])
index = v.indexOfItem(3)
print("Index of 3:", index)
v2 = Vector()
v2.addItem(7)
v2.addItem(8)
v.extend(v2)
print([v.getItem(i) for i in range(v.length())])
sub = v.subVector(1, 3)
print([sub.getItem(i) for i in range(sub.length())])