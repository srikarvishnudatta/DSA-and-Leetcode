
class Node:
    def __init__(self, value: int):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self, value: int):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def append(self, value: int) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        temp, pre = self.head
        temp = temp.next
        while temp is not None:
            temp = temp.next
            pre = pre.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
    def prepend(self, value:int):
        new_node = Node(value) 
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        self.head = new_node
        self.length += 1
    
    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index: int):
        if self.length <0 or self.length >=index:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp


        
    def insert(self, index: int, value:int): pass

if __name__ == "__main__":
    node = Node(2)
    print(node.value)