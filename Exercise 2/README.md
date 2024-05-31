# Exercise 2

This Exercise is seperated in two parts:

### Histogram of mathematical sets:

The histogram function takes a **list of lists** and returns a **dictionary**
representing the frequency of each unique sorted tuple of elements,
effectively creating a histogram of mathematical sets. It processes each
sublist by sorting its elements and removing duplicates to form a tuple,
which is then used as a key in a dictionary to count its occurrences. 

For example, **histogram([["a", "b", "a"], ["b"], ["a", "b"]])** returns **{('a', 'b'): 2, ('b',): 1}**, 
indicating that the set **{'a', 'b'}** appears twice and the set **{'b'}** appears once.


### Permutations detector:

The isPermutation function checks whether two lists are permutations of each other, 
meaning they contain the same elements in any order.
It does this by first ensuring both lists have the same length and then verifying that
each element in the first list is present in the second list and vice versa. 

For instance,
**isPermutation([1, "test", 3.14159, [], True, []], [1, "test", 3.14159, [], True, "test"])** returns **False**, 
while **isPermutation([1, "test", 3.14159, [], True], ["test", True, [], 1, 3.14159])** returns **True**.