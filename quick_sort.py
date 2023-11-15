def quick_sort(array):
    mid = len(array) // 2
    if len(array) <= 1:
        return array
    else:
        pivot = array[mid]
        left = []
        right = []
        for i in array:
            
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
        print('left: ', left, end=' ')
        print('right: ', right)
        return quick_sort(left) + [pivot] + quick_sort(right)
    

lst = [4,2,6,8,5,9,1,3]
print(quick_sort(lst))
# print(quick_sort([4,2,6,8,5])