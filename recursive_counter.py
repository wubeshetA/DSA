"""A recursive function to count the number of items in a list"""

def counter(lst):
    
    # Base case
    if len(lst) == 0:
        return 0
    return 1 + counter(lst[1:])
    # Recursive case
    
lst = [1, 2, 3]
print(counter(lst))