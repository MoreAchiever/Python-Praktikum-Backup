# Exercise 2

This Exercise is seperated in three parts:

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

### Statistics:


This function statistics, calculates basic statistical measures such as
**mean**, **variance**, **median**, **minimum**, and **maximum** from a given dataset data. 
It starts by initializing variables for the sum and variance. Then,
it iterates through the dataset to calculate the sum of all elements. 
After computing the mean, it proceeds to calculate the variance using a second loop,
summing up the squared deviations from the mean, divided by the length of the dataset.
Next, it sorts the dataset in ascending order to find the median.
If the dataset has an odd number of elements, it selects the middle value as the median; 
otherwise, it averages the two middle values. Finally,
it constructs a dictionary containing the calculated statistics and returns it.

When called with the sample dataset **[2, 4, 2.5, -1, 3]**, 
it returns a dictionary with keys **"mean", "variance", "median", "minimum", and "maximum"**, each corresponding to their respective statistical measures.