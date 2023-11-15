def selection_sort(lst):
    for i in range(len(lst)):
        # tranverse through the unordered list
        min = lst[i]
        min_index = i
        for j in range(i, len(lst)):
            if lst[j] < min: 
                min_index = j
                min = lst[j]
                
        # swap
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
                
                
            
        
if __name__ == '__main__':
    lst = [4,2,6,8,5,9,1,3]
    print(selection_sort(lst)