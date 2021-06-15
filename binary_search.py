# binary search implementation using loop
def search(lst, n, key):
	low = 1
	high = n
	while (low <= high):
		mid = (low + high)//2
		if (key == lst[mid]):
			return mid
		elif (key > lst[mid]):
			low = mid+1
		else:
		 	high = mid-1
	return 0		
A = [4,5,7,8,9,20,30,54,96]
print(search(A, len(A), 9))
)



