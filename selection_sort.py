"selection sort implementation"
from random import randint


def select_sort(array):

    # steps
    # 1. traverse through the list while comparing each element
    # traverse 1 time less that the previous on each traverese

    # 2. pick the max element
    # 3. remove it from the original array and
    # add it to the new array (array to be returned)
    return_array = []
    for i in range(len(array)):
        max = array[0]
        max_index = 0
        for j in range(len(array)):
            if array[j] >= max:
                max = array[j]
                max_index = j
        return_array += [max]
        array.pop(max_index)

    return return_array


array = [2, 6, 3, 6, 29, 4, 1, 4, 10]
# print(select_sort(array))

lst = []
for i in range(20):
    lst.append(randint(1, 100))

print(lst)
print(select_sort(lst))
