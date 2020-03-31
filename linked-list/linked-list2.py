# Remove Dups
# Write code to remove duplicates from an unsorted linked list

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

def printLL(head):
	while(head != None):
		print(head.data)
		head = head.next

a = Node(2)
a.appendToTail(3)
a.appendToTail(4)
a.appendToTail(3)
a.appendToTail(2)
a.appendToTail(1)
a.appendToTail(1)
a.appendToTail(3)
a.appendToTail(2)
a.appendToTail(5)
a.appendToTail(7)
a.appendToTail(5)

def removeDuplicates(head):
	dict = {}
	n = head
	print("Initiate")
	printLL(a)
	print("Go")
	while(n.next != None):
		if(not n.data in dict):
			dict[n.data] = 1
		if(n.next.data in dict):
			while(n.next != None and n.next.data in dict):
				if(n.next.next != None):
					n.next = n.next.next
				else:
					n.next = None
				n = n.next
		else:
			n = n.next

removeDuplicates(a)
print("Done")
printLL(a)

# 2 -> 3 -> 4 -> 3 -> 2 -> 5
