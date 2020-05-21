class Stack:
  def __init__(self):
    self.stack = []
    self.total = 0

  def push(self, element):
    self.stack.append(element)
    self.total = len(self.stack)
    return self.stack

  def pop(self, data):
    for i in range(self.total-1, -1, -1):
      if self.stack[i] == data:
        self.stack.pop()
        self.total = len(self.stack)
        return self.stack
      self.stack.pop()
    
    return self.stack

  def size(self):
    return self.total

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.stack)

stack.pop(3)
print(stack.stack)