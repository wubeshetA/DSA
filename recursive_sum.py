"""
A recursive function to sum a list of numbers.
it is a part of devide and conquer algorithm.
"""
def sum(lst):
    # Base case
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    
    # Recursive case
    return lst[0] + sum(lst[1:])

lst = [1, 2, 3, 4]
print(sum(lst))