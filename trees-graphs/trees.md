# Trees

## What is a tree?
A tree is a data structure composed of **nodes** that can be described with the following recursive explanation:
- Each tree has a root node
- The root node has zero or more child nodes
- Each child node has zero or more childs, and so on
A node is called a **leaf** if it has no children

## Binary tree
A **binary tree** is a tree where each node has up to two children

### Binary search tree
A **binary search tree** is a binary tree that has the property:
> For each node n, all left descendents <= n < all right descendents
(note that this inequality must be true for **all of a node's descendents**, not just its immediate children)

### Balanced vs Unbalanced
A **balanced tree** is "not terribly imbalanced". It is balanced enough to ensure **O(log n)** times for *insert* and *find*.

### Complete binary tree
A **complete binary tree** is a binary tree in which every level of the tree is fully filled, except maybe for he last level (to the right).

### Full binary tree
A **full binary tree** is a binary tree in which every node das either 0 or two children.

### Perfect binary tree
A **perfect binary tree** is both *full* and *complete*.

## Binary tree traversal

### In-order traversal
The most common kind. Consists in "visiting" the left branch, then the current node, and finally the right branch.
It is called **in-order** because if performed on a binary search tree, it visits the nodes in ascending order.

### Pre-order traversal
Visits the current node, then the left branch and finally the right branch. The root node is the first visited.

### Post-order traversal
Visits the left branch, then the right branch and finallt the current node. The root node is the last visited. 

## Binary heaps
A **min-heap** is a complete binary tree where each node is smaller than its children. The root is the minimal element in the tree. 

## Tries (Prefix trees)
A **trie** is a variant of a *n-ary tree* in which:
- characters are stored at each node
- each path down the tree may represent a word
- the * node are used to indicate a complete word
Tries are useful for quick prefix lookups. A trie can check if a string is a valid prefix in O(k) tie, where k is the length of the string (same as a hash table).