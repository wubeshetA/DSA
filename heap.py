# implementation of heap data structure
# this desmostration considers max heap

def h_create(lst):
    pass
def h_insert(lst, element):
    """"
    here is the algorithm to implement.
    # 1. add element to lst
    # 2. adject element's position in the heap 
        # compare element with it's ancestor/parent/root in the tree representation of the list.
            # if element <= ancestor then element is in its correct position
            # else if element > ancestor then 
                # swap element and ancestor
                # do the above until element is in its correct position
    """
    lst += [element]
    i = 1
    ancestor_pos = (len(lst)//(i*2))-1 # element's ancestor position
   
    while(element > lst[ancestor_pos] and ancestor_pos >= 0):

        elmt_pos = (len(lst)//i) - 1
        lst[ancestor_pos], lst[elmt_pos] = lst[elmt_pos], lst[ancestor_pos]
        i *= 2
        ancestor_pos = (len(lst)//(i*2))-1
    return lst     

def h_delete():
    pass
def h_sort(lst):
    pass
heap = [70, 60, 50, 40, 30, 20, 10]
# heap2 = [80, 70, 50, 60, 30, 20, 10, 40]
# heap3 = [90, 80, 50, 70, 30, 20, 10, 40, 60]
# heap4 = [100, 90, 50, 70, 80, 20, 10, 40, 60, 30]
# heap5 = [110, 100, 50, 70, 90, 20, 10, 40, 60, 30, 80]
a = [60]
for i in a:
    heap = h_insert(heap, i) 
print(heap)
# print(h_insert(heap, 40))

