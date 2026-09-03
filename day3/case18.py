#find the maximum number of consecutive 1s in a binary array

def findmax(nums):
    max_count = 0
    count = 0
    
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
            
    return max_count
nums = [1, 1, 0,1,1, 1,1,0, 1, 1]    
print(findmax(nums))