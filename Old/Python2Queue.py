

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the item at the front of the queue. Raises an exception if the queue is empty."""
        if self.is_empty():
            raise Exception("Queue is empty. Cannot dequeue.")
        return self.items.pop(0)

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise."""
        return len(self.items) == 0

    def size(self):
        """Returns the number of items in the queue."""
        return len(self.items)


mytesting_queue = Queue()

print(mytesting_queue.is_empty())

mytesting_queue.enqueue(1)
mytesting_queue.enqueue(2)
mytesting_queue.enqueue(3)
mytesting_queue.enqueue(4)
mytesting_queue.enqueue(5)

print(mytesting_queue.size())
print(mytesting_queue.dequeue())
print(mytesting_queue.dequeue())