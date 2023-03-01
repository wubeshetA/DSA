def b_search (array, item):
    low = 0
    high = len(array) - 1
    
    while (low <= high):
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1

            
            
    

# list of array from 1- 20
array = range (1, 100000)
print(b_search(array, 26))
