def quick_sort(lst):
    # base case
    # list is sorted if len(lst) is less 2
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left = []
        right = []
        for i in lst[1:]:
            if i >= pivot:
                right.append(i)
            else:
                left.append(i)
        print("{} <{}> {}".format(left, pivot, right))
        return quick_sort(left) + [pivot] + quick_sort(right)
                
    # recursive case
    
if __name__ == "__main__":
    lst = [9, 3, 5, 1, 6]
    print(quick_sort(lst))
    # excution process
    """
    [] <> []
    
    
    lst = [9, 3, 5, 1, 6]
    return [3, 5, 1, 6] + <9> + [] ---> return ([3, 5, 1, 6]) + [9] + []
    
    lst = [3, 5, 1, 6]
    return [1] + <3> + [5, 6]  ---> [1] + [3] + return ([5, 6]) --> [1, 3, 5, 6]
    
    lst = [5, 6]
    return [] + <5> + [6] ---> return [] + return [5] + return [6] = [5, 6]
    [] <> []
    """