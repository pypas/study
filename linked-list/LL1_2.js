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

function removeDuplicates(head) {
	let p1 = head
	let p2 = head.next
	head.next = p2

	while(p1 != null) {
		p2 = p1
		while(p2.next != null) {
			if(p2.next.data == p1.data) {
				p2.next = p2.next.next
			} else {
				p2 = p2.next
			}
		}

		p1 = p1.next
	}
	return head
}

let head = new Node(3);
head = createLinkedList(head, [2,3,4,3,5,2,6,7,5]);
head = removeDuplicates(head);
printLinkedList(head);

//O(1) space, O(N²) time