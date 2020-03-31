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
	let dict = {};
	dict[head.data] = 1
	let n = head.next;
	while(n != null) {
		if(dict[n.data] == null) {
			dict[n.data] = 1;
		}
		let prox = n.next
		if(dict[prox.data] != null) {
			while(prox != null && dict[prox.data] != null) {
				prox = prox.next
			}
			n.next = prox
		}

		n = prox
	}
	return head
}

let head = new Node(3);
head = createLinkedList(head, [2,3,4,3,5,2,6,7,5]);
head = removeDuplicates(head);
printLinkedList(head);

//O(N)