// Delete middle node
// Delete a node in the middle (any node but the first or the last) given only access to that node 

class Node {
	next = null;
	data;

	constructor(d){
		this.data = d;
	}

	appendToTail(d){
		let end = new Node(d);
		let n = this;
		while(n.next != null) {
			n = n.next;
		}
		n.next = end;
	}

}

function printLinkedList(head) {
	while(head != null) {
		console.log(head.data);
		head = head.next;
	} 
}

function createLinkedList(head, list) {
	for(item of list) {
		head.appendToTail(item);
	}
	return head
}

function deleteMiddleNode(current) {
	// We're going to "pretend" we deleted that node
	let node = current
	while(node.next != null) {
		node.data = node.next.data
		if(node.next.next == null) {
			node.next = null
		} else {
			node = node.next
		}
		

	}
	return current
}
let head = new Node(1);
let middle1 = new Node(2);
let middle2 = new Node(3);
let middle3 = new Node(4);
let end = new Node(5);
head.next = middle1;
middle1.next = middle2;
middle2.next = middle3;
middle3.next = end;
middle1 = deleteMiddleNode(middle2);
printLinkedList(head)

//O(N)