class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)


# Example Usage:

# Stack
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

# print("Stack:")
# print("Top:", stack.peek())
# print("Pop:", stack.pop())
# print("Pop:", stack.pop())
# print("Size:", stack.size())

# # Queue
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)

# print("\nQueue:")
# print("Front:", queue.front())
# print("Dequeue:", queue.dequeue())
# print("Dequeue:", queue.dequeue())
# print("Size:", queue.size())
# 