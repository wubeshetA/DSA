"""
A recursive function to sum a list of numbers.
it is a part of devide and conquer algorithm.
"""


def sum(lst):
    # Base case
    if len(lst) == 0:
        return 0

    # Recursive case
    return lst[0] + sum(lst[1:])


lst = [1]
print(sum(lst))
