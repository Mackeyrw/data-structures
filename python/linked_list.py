class LinkList:
  def __init__(self, head=None):
    self.head = head
    self.length = 0

  def add_node(self, data):
    new_node = Node(data)
    if self.head == None:
        self.head = new_node
    else:
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
    
  def remove(self, data):
    current_node = self.head
    previous_node = None
    if current_node.data == data:
      self.head = current_node.next_node
    else:
      while current_node.data != data:
        previous_node = current_node
        current_node = current_node.next_node
      previous_node.next_node = current_node.next_node
    return self.head
    
  def get(self, data):
    current_node = self.head
    while current_node.data != data:
      current_node = current_node.next_node
    return current_node.data

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

new_linked = LinkList()
print(new_linked.head)
new_linked.add_node(4)
print(new_linked.head.data)
new_linked.add_node(7)
new_linked.add_node(9)
new_linked.remove(4)
print(new_linked.head.data)
new_linked.add_node(5)
new_linked.add_node(6)
print(new_linked.get(5))