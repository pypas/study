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

	def deleteNode(self, head, d):
		n = head

		if(n.data == d):
			return head.next

		while(n.next != None):
			if(n.next.data == d):
				n.next = n.next.next
				return head
			n = n.next
		return head


a = Node(2)
a.appendToTail(3)
a.deleteNode(a,3)
a.appendToTail(4)
print(a.next.data)