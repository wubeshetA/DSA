
# implementation of heap data structure
# this desmostration considers max heap


def h_insert(lst, element):
    """"
    here is the algorithm to implement.
    # 1. add element to lst
    # 2. adjust element's position in the heap 
        # compare element with it's ancestor/parent/root in the tree representation of thdata_structure_and_algorithmse list.
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
    # return lst     

# return deleted element(root element) of the heap
def h_delete(lst):
    """
    algorithm to implement:
    1. delete the first element of the heap (the main root in the tree representation of the heap)
    2. adjust the postition of the elements so that it create max heap
        # move the last element to position of the deleted element - this can be done by swaping the last and the first element instead of totally removing the first element out of the array. (it will also be used for later usage in heap sort function).
        # then compare each ancestor element with descendants and if one of the descendant is greater that the ancestor swapt them. If not the array is heap.
    """
    deleted = lst[0]
    lst[0], lst[-1] = lst[-1], lst[0] # swaping the 1st & last element. now the first element is no more part of the unadjusted heap.
    
    lst.pop()
  
    # compare ancestor to (2*i) and (2*i+1) position (to the descendant)
        # if ancestor less than one of the descendants then,
            # compare the descendats,
            # move the greater descendat up on the binary tree represantation of unadjusted heap.
    # do the above until the list become max heap

    des_pos1 = 1#2 * i - 1 # this is the (2*i)th position of he descendeant in the above algorithm
    des_pos2 = 2 # 2 * i # this is the (2*i + 1)th position
    ancs_pos = 0 # anscestor position

    if len(lst) <=  1:
        pass
    elif len(lst) == 2:
        if (lst[0] < lst[1]):
            lst[0], lst[1] = lst[1], lst[0]

    else:        
        while(lst[ancs_pos] < lst[des_pos1] or lst[ancs_pos] < lst[des_pos2]):
       
            if (lst[des_pos1] > lst[des_pos2]):
                lst[ancs_pos], lst[des_pos1] = lst[des_pos1], lst[ancs_pos]
                ancs_pos = des_pos1
            else:
                lst[ancs_pos], lst[des_pos2] = lst[des_pos2], lst[ancs_pos]
                ancs_pos = des_pos2

            des_pos1 = 2 * (ancs_pos + 1) - 1
            des_pos2 = 2 * (ancs_pos + 1)

            # Stop adjusting when there is no other node.
            if (des_pos1 >= len(lst) or des_pos2 >= len(lst)):
                break
    return deleted

# h_create - create a heap from a list
# return: created heap
def h_create(lst):
    heap = []
    for i in lst:
        h_insert(heap, i)
    return heap

# h_sort - sort a list
# return: a sorted list
def h_sort(lst):
    heap = h_create(lst)
    sorted_list = []

    for i in range(len(heap)):
        a = h_delete(heap)
        sorted_list += [a]

    sorted_list.reverse()    
    return sorted_list
       
def main():
    # heap = [70, 60, 50, 40, 30, 20, 10]
    # heap2 = [80, 70, 50, 60, 30, 20, 10, 40]
    # heap3 = [90, 80, 50, 70, 30, 20, 10, 40, 60]
    # print(h_sort(heap))
    # h_delete(heap)
    # print(heap)

    
    # print("created heap:", h_create(a))
    # heap4 = [100, 90, 50, 70, 80, 20, 10, 40, 60, 30]
    # heap5 = [110, 100, 50, 70, 90, 20, 10, 40, 60, 30, 80]

    unsorted = [10, 30, 20, 60, 2, 100, 35,34, 120, 50, 70, 40]
    sorted = h_sort(unsorted)
    print(sorted)
    a = input("type st")
    print(a)

if __name__ == "__main__":
    main()
