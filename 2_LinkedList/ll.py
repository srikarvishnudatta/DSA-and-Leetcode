
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


        
    def set(self, index: int, value:int): 
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value): 
        if index < 0 and index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index)
        node = Node(value)
        node.next = temp.next
        temp.next = node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 and index>=self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    def reverse(self):
        curr = self.head
        prev = None

        while curr is not None:
            curr_node = curr.next

            curr.next = prev
            prev = curr

            curr = curr_node

        return prev
if __name__ == "__main__":
    node = Node(2)
    print(node.value)