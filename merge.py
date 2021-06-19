def merge(lst1, lst2):

    merged_lst = []
    i = 0
    j = 0
    while True:
        if i > len(lst1)-1:
            merged_lst += lst2[j:]
            break
        if j > len(lst2)-1:
            merged_lst += lst1[i:]
            break
        if lst1[i] == lst2[j]:
            merged_lst.append(lst1[i])
            merged_lst.append(lst1[i])
            i+=1
            j+=1
        if lst1[i] < lst2[j]:
            merged_lst.append(lst1[i])
            i+=1
        elif lst2[j] < lst1[i]:
            merged_lst.append(lst2[j])
            j+=1 
    return merged_lst
print(merge([0,1,4,6,7,8], [1,3,5,7,9,11,13,15]))    

