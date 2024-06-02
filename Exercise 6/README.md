# Exercise 6


This exercise practices **database schema design**, **SQL operations**,
interaction with **SQLite** in Python, object-oriented programming, 
and handling **timestamps**. The script sets up an in-memory SQLite database to manage email data,
including tables for **emails**, **mailboxes**, and **contacts**.
It first establishes a database connection and defines SQL statements to create the necessary tables.
The Email class is defined to represent email objects with attributes for **mailbox**, **sender**, **subject**, **content**
, and **timestamp**.
Utility functions are provided to generate **unique IDs**, list emails by mailbox, create new email entries,
and convert between timestamp formats. The listEmails function retrieves and formats emails from the database,
while createEmail inserts new emails. The script includes test data to demonstrate functionality,
showcasing basic CRUD operations and data manipulation within SQLite. 
This exercise provides hands-on experience with database management
and the integration of Python code to perform database operations.