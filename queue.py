class Queue(object):
    def __init__(self):
        self.queue = []

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        self.queue.pop(0)

    def enqueue(self, item):
        self.queue.append(item)

    @property
    def size(self):
        return len(self.queue)


example = Queue()

example.enqueue(5)
example.enqueue(2)
example.enqueue(3)
example.enqueue(1)

print(example.queue)
print(example.size)
example.dequeue()
example.dequeue()

print(example.queue)
print(example.size)
