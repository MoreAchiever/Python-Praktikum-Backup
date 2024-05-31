# Exercise 1 

This exercise is divided into three parts, each focusing on different aspects of Python programming: 

### Cross sum:
The function **quersumme(n, b)** calculates the sum of the digits of a number **n** in a given base **b**. It starts by initializing a sum variable to zero. Then, it repeatedly finds the last digit of n in base **b**, adds this digit to the sum, and removes the last digit from **n** by dividing **n** by **b** and discarding the remainder. This process continues until **n** becomes zero. Finally, the function returns the sum of the digits.

For example, when you call **quersumme(212, 10)**, it processes the digits of **212** in base **10** (which are **2**, **1**, and **2**), sums them up to get **5**, and returns this result.

### String Histogram: 

The function **histogram(strings)** takes a list of strings and counts how often each string appears in the list. It creates an empty dictionary, then iterates over the list of strings. For each string, if it is not already in the dictionary, it adds the string as a key and sets its value to the number of times the string appears in the list. Finally, the function returns the dictionary with these counts.

For example, when you run **histogram(["foo", "bar", "check", "foo", "check", "door"])**, it returns **{'foo': 2, 'bar': 1, 'check': 2, 'door': 1}**, indicating how many times each string appears in the list.

### List Comprehension:

The function **comprehend(a)** processes a list of strings and returns a new list containing the uppercase versions of those strings, excluding any strings that start with the letter **"z"** or **"Z"**. 

For example, when given **["Hallo", "Welt", "Zeitung", "lesen"]**, it returns **['HALLO', 'WELT', 'LESEN']**, excluding **"Zeitung"** because it starts with **"Z"**.






