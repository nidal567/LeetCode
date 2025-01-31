class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def add_node(self, head, val):
        new_node = Node(val)
        
        if head.next == head:
            head.prev = new_node
            head.next = new_node
            new_node.prev = head
            new_node.next = head
            return
    
        new_node.prev = head
        new_node.next = head.next
        
        new_node.next.prev = new_node
        head.next = new_node
        
        
head = Node(-1)
head.next = head
head.prev = head

head.add_node(head, 0)
head.add_node(head, 1)
head.add_node(head, 2)

current = head

while current:
    print(current.val)
    current = current.prev