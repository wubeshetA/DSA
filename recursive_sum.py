"""
A recursive function to sum a list of numbers.
it is a part of devide and conquer algorithm.
"""


def recursive_sum(lst):
    # Base case
    if len(lst) == 1:
        return lst[0]
    return lst[0] + recursive_sum(lst[1:])
    
    # recursive case
    1 + return recursive_sum([2, 3, 4])
    1 + 2 + return recursive_sum([3, 4])'"""""""""""" '


lst = [1, 2, 3, 4]
print(sum(lst))
