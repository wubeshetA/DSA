"""Quick sort implementation.
Using the Divide and Conqur method.
"""


def quick_sort(lst):

    # Base case
    if len(lst) < 2:
        return lst
    # Recursive case
    else:
        # pick pivot
        pivot = lst[0]

        # find elements smaller and larger than the pivot
        left = []
        right = []
        for elmt in lst[1:]:
            if elmt <= pivot:
                left += [elmt]
            else:
                right += [elmt]
        return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    lst = [13, 23, 6, 3, 7]
    print(quick_sort(lst))