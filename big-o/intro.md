# Big O

## What is Big O?
> Big O is the language and metric we use to decribe the efficiency of algorithms
> \- Gyle Laakmann Mcdowell, *Craking the coding interview* 

## Big O, Big Theta, Big Omega
- Big O: upper bound on the time.
Ex: Print all values in an array = O(N), but also O(N²), O(N³)...
- Big Omega: lower bound on the time.
Ex: Print all values in an array = omega(N) but also omega(log N), omega(1)...
- Bit Theta: means both Big O and Big Omega

### Best case, worst case, expected case
Using the example of Quick Sort
- Best case: O(N)
All elements are equal, quicksort just traverse through the array
- Worst case: O(N²)
The pivot is always the biggest element, so the recursion doesn't divide de array in half
- Expected case: O(N*logN)
Suppose the partition breaks the input in half at each time. The number of times we can break it in half is log N 
(Ex: if the size of the array is 128, we get partitions of size 64,32,16,8,4,2 and 1, i.e. log2(128) = 7 levels of partitioning). Therefore, we get log N partitioning levels and for each level we visit N inputs, that is, O(N*logN).