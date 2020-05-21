class Queue:
  def __init__(self):
    self.total = 0
    self.queue = []

  def enqueue(self, element):
    self.queue.append(element)
    self.total = len(self.queue)
    return self.queue

  def dequeue(self, data):
    for i in range(self.total):
      if self.queue[i] == data:
        self.queue = self.queue[i+1:]
        self.total = len(self.queue)
        return self.queue

  def size(self):
    return self.total

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.queue)

queue.dequeue(3)
print(queue.queue)
print(queue.total)