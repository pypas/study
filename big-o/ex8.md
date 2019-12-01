Analyse the following algorithm
- Takes in an array (length a) of strings (length s)
- Sort each string
- Sorted the full array

Complexity:
- Sort each string: O(s*log s)
- Do this for every string in the array: O(a\*s\*log s)
- Remember that to compare each string, it takes O(s) time. 
There are O(a\*log a) comparisons to be done: O(a\*s\*log(s) + a\*s\*log(a)) 
The complexity is O(a\*s\*(log(a) + log(s)))