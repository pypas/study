// Return Kth to last
// Implement an algorithm to find the kth to last element of a singly linked list

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

function kthToLast(head, k) {
	let current = head
	let runner = current
	while (k > 0) {
		runner = runner.next
		k--;
	}
	while(runner.next != null) {
		current = current.next
		runner = runner.next
	}
	return current.data
}

let head = new Node(3);
head = createLinkedList(head, [2,3,4,3,5,2,6,7,5]);
k = 3;
console.log(kthToLast(head, k))

// O(N) time, O(1) space