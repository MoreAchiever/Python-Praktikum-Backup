# Exercise 4

This exercise covers three key concepts in programming: **Object-Oriented Programming (OOP)**, **Encapsulation**, and **Inheritance**. And it is divided in three parts

### Statistics (object oriented):

This exercise part revisits the statistical calculations introduced in [Exercise 2](../Exercise%202),
now implemented within a class structure.
It demonstrates the application of OOP principles by encapsulating statistical operations within methods of a class.

### Incapsulation and Inheritance in Library setting:

This part simulates a simplified library by encapsulating common attributes and methods in a **Product** class,
which serves as a base for more specialized classes like **Book** and **Computer**. 
These subclasses inherit attributes and methods from Product, illustrating inheritance.
Encapsulation is observed in how data is stored within objects and accessed only through methods,
ensuring data integrity and abstraction. 
This script exemplifies encapsulation and inheritance within the context of managing library inventory.

### Bijection:


This Python code defines a Bijection class, which facilitates bijective mappings between two sets of values.
It practices several object-oriented programming (OOP) concepts such as encapsulation,
inheritance, and method overloading.
The Bijection class encapsulates two dictionaries (dict1 and dict2) to represent the mapping in both directions.
The constructor **(__init__)** initializes these dictionaries based on the input provided,
checking for duplicates if the input is a dictionary. The class overrides several operators,
including string representation **(__str__)**, item access **(__getitem__)**, item assignment **(__setitem__)**,
and item deletion **(__delitem__)**. The **__mul__** method enables function composition,
combining two bijections into a new one. Additionally,
the inverse method returns a new Bijection object representing the inverse mapping.
The code demonstrates the creation, manipulation, and composition of bijections,
emphasizing OOP principles such as encapsulation and method overloading to manage bijective mappings effectively.