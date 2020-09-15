class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(new_node)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return None

    def size(self):
        return len(self.stack)

    def __len__(self):
        return self.size()

    def is_empty(self):
        return len(self.stack) == 0


new_node = Node("Stack")
another_node = Node("Stack2")

stacks_on_stacks = Stack()
stacks_on_stacks.push(new_node)
stacks_on_stacks.push(another_node)

print(stacks_on_stacks)

stacks_on_stacks.pop()
print(stacks_on_stacks)

stacks_on_stacks.push(Node("Stack3"))

print(stacks_on_stacks.size())

print(stacks_on_stacks.is_empty())