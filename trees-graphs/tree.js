class Node {
	right = null
	left = null
	constructor(name, left, right) {
		this.name = name;
		this.left = left;
		this.right = right;
	}
}

let f = new Node("20", null,null)
let d = new Node("2", null,null)
let e = new Node("6", null,null)
let c = new Node("10", null,f)
let b = new Node("4", d,e)
let a = new Node("8", b,c)

function inOrderTraversal(node) {
	if(node != null) {
		inOrderTraversal(node.left)
		console.log(node.name)
		inOrderTraversal(node.right)
	}
}

function preOrderTraversal(node) {
	if(node != null) {
		console.log(node.name)
		preOrderTraversal(node.left)
		preOrderTraversal(node.right)
	}
}

function postOrderTraversal(node) {
	if(node != null) {
		postOrderTraversal(node.left)
		postOrderTraversal(node.right)
		console.log(node.name)
	}
}

console.log("In order traversal")
inOrderTraversal(a)
console.log("Pre order traversal")
preOrderTraversal(a)
console.log("Post order traversal")
postOrderTraversal(a)