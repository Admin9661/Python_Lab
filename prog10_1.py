def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def mergesort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums)//2
    return merge(mergesort(nums[:mid]),mergesort(nums[mid:]))


    
nums = [23,12,43,67,4,5,14]
print(mergesort(nums))