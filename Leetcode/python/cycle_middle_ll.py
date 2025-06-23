def cycle(head):
    slow, fast = head, head
    while fast:
        slow = slow.next
        if not fast.next: return False
        fast = fast.next.next
        if slow == fast: return True
    return False

def middle(head):
    slow, fast = head, head
    while fast:
        fast = fast.next.next
        slow = slow.next
    return slow