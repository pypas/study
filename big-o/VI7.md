If a binary search tree is not balanced, how long might it take (worst case) to find an element in it?


- Height
The height of a node in a tree is the length of the longest path from that node downward to a leaf, counting both the start and end vertices of the path. The height of a leaf is 1. The height of a nonempty tree is the height of its root.

- Height-balancement
A node in a tree is height-balanced if the heights of its subtrees differ by no more than 1. (That is, if the subtrees have heights h1 and h2, then |h1 − h2| ≤ 1.) A tree is height-balanced if all of its nodes are height-balanced. 

Go through all elements: O(N)