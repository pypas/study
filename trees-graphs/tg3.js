// List of depths
// Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
// (e.g. if you have a tree with depth D, you'll have D linked lists)

class Node {
	right = null
	left = null
	constructor(name, left, right) {
		this.name = name;
		this.left = left;
		this.right = right;
	}
}

class NodeLL {
	next = null;
	data = null;

	constructor(d){
		this.data = d;
	}
}

let f = new Node("20", null,null)
let d = new Node("2", null,null)
let e = new Node("6", null,null)
let c = new Node("10", null,f)
let b = new Node("4", d,e)
let root = new Node("8", b,c)


