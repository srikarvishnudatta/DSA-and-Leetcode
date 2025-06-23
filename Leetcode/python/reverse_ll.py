

def reverseLL(head):
    # iterative
    prev, curr = None,head
    while curr:
        temp = curr.next
        prev = curr
        curr.next = None
        curr = temp
    return prev

def recursion(head):
        if not head:None
        new_head = recursion(head.next)
        head.next.next = head.next
        head.next = None
        return new_head