lines = [ ] 
"""
This script demonstrates a simple example of a queue using a list in Python.

The script performs the following operations:
1. Initializes an empty list named 'lines'.
2. Appends four names to the list.
3. Removes the first element from the list (FIFO - First In, First Out).
4. Prints the remaining elements in the list.

This is an example of a queue data structure.
"""
lines.append('Musa') 
lines.append('Ibrahim') 
lines.append('Alhaz') 
lines.append('Bappy') 
lines.pop(0) 
print(lines)
