
def productExceptSelf(nums):
    
    # =====BRUTE FORCE METHOD======
    # for i in range(len(nums)):
    #     prefix_prod = 1
    #     for k in range (i-1, -1, -1):
    #         prefix_prod *= nums[k]
    #     post_prod = 1
    #     for j in range(i+1, len(nums)):
            
    #         post_prod *= nums[j]
    #     solution.append(prefix_prod * post_prod)
    
    # return solution
    
    # ============ FASTER METHOD ====
    # ===time complexity = O(n), space complexity = O(1)
    length = len(nums)
    solution = [1] * length
    # nums = [1,2,3,4]
    pre = 1
    post = 1
    for i in range(length):
        solution[i] = solution[i] * pre
        pre = pre * nums[i]
        solution[length-i-1] = solution[length-i-1] * post
        post = post * nums[length-i-1]
    return solution


lst = [1,2,3,4]
print(productExceptSelf(lst))
for a in range(2, -1, -1):
    print(a)

