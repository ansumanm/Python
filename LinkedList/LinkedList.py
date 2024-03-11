class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.root = None

  def insert(self, value):
    newNode = Node(value)

    if self.root is None:
      self.root = newNode
    else:
      # Insert at front.
      newNode.next = self.root
      self.root = newNode

  def reverse(self):
    currNode = self.root
    prevNode = None
    # 1->2->3->4
    while(currNode):
      # 1. Store the next node
      nextNode = currNode.next

      # 2. Point current node to previous node
      currNode.next = prevNode

      # 3. Root always points to the current Node
      self.root = currNode

      # 4. Move the previous node to the current Node
      prevNode = currNode

      # 5. Move the current node to the next node.
      currNode = nextNode


  def printList(self):
    tmpNode = self.root
    ll = []
    while tmpNode:
      ll.append(tmpNode.value)
      tmpNode = tmpNode.next

    print(f"{('->'.join([str(node) for node in ll]))}")

  def sortList(self):
    """
    Problem statement: Sort Linked List which is alread sorted on actual values.
    Input: 1 -> -2 -> -3 -> 4 -> -5
    Output: -5 -> -3 -> -2 -> 1 -> 4
    """
    continueLoop: bool = True
    loopCounter = 0
    sortedCheckpoint = None # The Node in the list after which rest of the nodes are sorted.

    while continueLoop:
      loopCounter += 1
      continueLoop = False
      tmpNode = self.root
      
      print("--------------")
      self.printList()
      print("--------------")

      while tmpNode:
        if sortedCheckpoint and tmpNode == sortedCheckpoint:
          print(sortedCheckpoint.value)
          break

        nextNode: Node = tmpNode.next
        if nextNode is None:
          break
        if tmpNode.value > nextNode.value:
          # Sort them by swapping the values
          tmpValue = tmpNode.value
          tmpNode.value = nextNode.value
          nextNode.value = tmpValue
          continueLoop = True
          sortedCheckpoint = tmpNode

        tmpNode = tmpNode.next

    print(f"Loop counter: {loopCounter}")


if __name__ == "__main__":
  ll = LinkedList()
  ll.insert(-5)
  ll.insert(4)
  ll.insert(-3)
  ll.insert(-2)
  ll.insert(1)

  print("Input List")
  ll.printList()
  ll.sortList()
  print("Sorted List")
  ll.printList()
  # ll.insert(1)
  # ll.insert(2)
  # ll.insert(3)
  # ll.insert(4)
  # ll.insert(5)
  # ll.insert(6)
  # ll.insert(7)
  # ll.insert(8)

  # ll.printList()
  # ll.reverse()
  # ll.printList()