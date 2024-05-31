# Exercise 3

This exercise introduces us to **parsing** and it consist of four parts:

### Tokenizer:

The tokenize function parses a given string into a list of tokens,
separating numerical values and mathematical symbols.
It iterates through each character in the string, validating that only digits,
parentheses, spaces, hyphens, and spaces are present; otherwise,
it raises an exception for invalid characters.
It constructs numerical tokens by appending consecutive digits and converts them into integers.
If non-numeric characters are encountered, they are added to the token list individually.
Finally, it returns the list of tokens.

For instance, **tokenize("(80-10) - (17-3)")** would return **[ '(', 80, '-', 10, ')', '-', '(', 17, '-', 3, ')' ]**,
representing the parsed tokens of the mathematical expression.

### Tokenizer recursively:

The tokenize function recursively parses a given string into a list of tokens, 
separating numerical values and mathematical symbols.
It initializes an empty list arr and an empty string temp,
then defines a nested function subtoken to handle the parsing process.
This function extracts numerical values from the string by appending consecutive digits to temp until encountering
a non-digit character. Upon encountering a non-digit character,
it adds the accumulated numerical token to the arr list and resets temp.
The tokenize function iterates through each character of the input string,
recursively calling subtoken when numerical characters are encountered and appending non-numeric characters directly to arr.
It ensures valid characters, including digits, parentheses, spaces, and hyphens, are processed,
raising an exception for invalid characters. Finally, it returns the list of tokens. 

tokenize("(80-10) - (17-3)-()") returns [ '(', 80, '-', 10, ')', '-', '(', 17, '-', 3, ')', '-', '(', ')' ],
The same result as in **Tokenizer (see first part)**.

### Parser:

The parser contains code for parsing mathematical expressions involving subtraction operations.
It imports the previously implemented tokenizer module, which provides functions for tokenizing input strings.
Within parser, a class named Subtraction is defined to represent subtraction operations,
offering initialization with left and right operands, string representation support,
and a method to execute the subtraction operation. Additionally, the file includes functions like parseMinus,
responsible for recursively parsing subtraction expressions from a list of tokens, handling nested parentheses,
and constructing the expression tree, as well as parse,
which coordinates the parsing process and ensures the entire token list is consumed. 
The code demonstrates the usage of these functions by parsing a subtraction expression,
evaluating it, and printing the result. 

For instance,
when given the input **"(40 - 5) - (18 - (13 - 10))"**, the code evaluates to **20** and prints **"(40 - 5) - (18 - (13 - 10))"**.


### Pascal's triangle:

The **loop(n)** function generates Pascal's triangle up to the specified number of rows **n**.
It initializes a 2D list arr with the first row containing only a single element 1.
Then, it iterates from the second row to the n-th row, constructing each row by appending 1 at the beginning and end,
with intermediate values set to None. Subsequently, it fills in the intermediate values by iterating through each row and column,
replacing None with the sum of the corresponding values from the previous row and the one diagonally above. 
Finally, it returns the completed Pascal's triangle stored as a 2D list.

When **loop(5)** is called, it prints Pascal's triangle up to the 5th row.