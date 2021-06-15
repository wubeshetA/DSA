# Binary search algorithm implmentations
# using recursion
def search(lst, l, h, key):	
	mid = (l + h)//2
	if (key == lst[mid]):
		return mid
	elif (l > h):
		return 0
	elif (key > lst[mid]):
		l = mid + 1
	elif (key < lst[mid]):
	 	h = mid -1
	return search(lst, l, h, key)	


A = [1,2,3,6,7,8,9,15,16,33]
print(search(A, 1, len(A),16))



def search2(lst, l, h, key):
	if (l == h):
		if (lst[l] == key):
			return l
		else:
		 	return 0
	else:
		mid = (l + h)//2
		if (key == lst[mid]):
			return mid
		if (key > lst[mid]):
			print('high')
			return search2(lst, mid+1, h, key)
		else:
			print('low')
			return search2(lst, l, mid-1, key)
print(search2(A, 1, len(A), 16))
