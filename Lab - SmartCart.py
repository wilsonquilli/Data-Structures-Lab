#SmartCart - A Shopping Cart Data Structure, that combines a Linked List and Dictionary.
#Made for speed, organization, and efficiency for better UX/UI

#Node Class with parameters needed for SmartCart
class Node:
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
        self.next = None

#SmartCart Class (My New Data Structure)
class SmartCart:
    def __init__(self):
        self.head = None
        self.tail = None
        self.index = {}  #Dictionary

    #Add Items function
    def add_item(self, item, price, quantity = 1):
        if item in self.index:
            self.index[item].quantity += quantity
            return
        node = Node(item, price, quantity)
        self.index[item] = node
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    #Update Item Function
    def update_item(self, item, new_quantity):
        if item in self.index:
            self.index[item].quantity = new_quantity
            if new_quantity <= 0:
                self.remove_item(item)

    #Remove Item Function
    def remove_item(self, item):
        if item not in self.index:
            return
        target = self.index[item]
        prev, cur = None, self.head
        while cur:
            if cur is target:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                if cur is self.tail:
                    self.tail = prev
                del self.index[item]
                return
            prev, cur = cur, cur.next  

    #Total Items in my SmartCart Function
    def total_items(self):
        count = 0
        cur = self.head
        while cur:
            count += cur.quantity
            cur = cur.next
        return count
    
    #Price of all items combined Function
    def total_price(self):
        total = 0.0
        cur = self.head
        while cur:
            total += cur.price * cur.quantity
            cur = cur.next
        return total
    
    #Lists all items in SmartCart function
    def list_items(self):
        items = []
        cur = self.head
        while cur:
            items.append((cur.item, cur.price, cur.quantity))
            cur = cur.next
        return items

#Test
cart = SmartCart()
cart.add_item("Iphone 17", 999.00, 1)
cart.add_item("Airpods Pro", 249.00, 1)
cart.add_item("Shirt", 10.00, 2)
cart.update_item("Shirt", 3)
cart.remove_item("Airpods Pro")
print("Items in Order:", cart.list_items())
print("\nTotal Items:", cart.total_items())
print("\nTotal Price:", round(cart.total_price(), 2))