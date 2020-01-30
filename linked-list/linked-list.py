# Linked List
class Node:
	next = None
	data = None

	def __init__(self,d):
		self.data = d

	def appendToTail(self,d):
		end = Node(d)
		n = self
		while(n.next != None):
			n = n.next
		n.next = end


a = Node(2)
a.appendToTail(3)
print(a.next.data)