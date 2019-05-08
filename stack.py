class Stack(object):
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    @property
    def size(self):
        return len(self.stack)


example = Stack()
example.push(1)
example.push('hello')
example.push(7)
example.push(True)

print(example.stack)
print(example.size)

example.pop()
example.pop()

print(example.stack)
print(example.size)
