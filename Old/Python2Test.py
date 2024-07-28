
#Task: Implement a method remove(data) in the LinkedList class that removes the
# first occurrence of a node with the specified data from the list.


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def remove(self, data):
        # If the list is empty
        if not self.head:
            return

        # If the node to be removed is the head
        if self.head.value == data:
            self.head = self.head.next
            return

        # Initialize pointers
        current = self.head
        prev = None

        # Traverse the list to find the node to be removed
        while current and current.value != data:
            prev = current
            current = current.next

        # If the node was found, remove it
        if current:
            prev.next = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')


# Usage Example
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

print("Original list:")
linked_list.print_list()

# Remove a node with value 3
linked_list.remove(3)

print("List after removing 3:")
linked_list.print_list()

# Remove a node with value 1 (head)
linked_list.remove(1)

print("List after removing 1 (head):")
linked_list.print_list()

# Remove a node with value 4 (tail)
linked_list.remove(4)

print("List after removing 4 (tail):")
linked_list.print_list()