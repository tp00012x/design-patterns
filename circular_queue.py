class CircularQueue(object):
    def __init__(self, k):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = k

    def enqueue(self, data):
        if self.size() == self.maxSize - 1:
            return "Queue Full!"
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return True

    def dequeue(self):
        if self.size() == 0:
            return "Queue Empty!"
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data

    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head


q = CircularQueue(8)
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q.enqueue(5))
print(q.enqueue(6))
print(q.enqueue(7))
print(q.enqueue(8))
print(q.enqueue(9))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
