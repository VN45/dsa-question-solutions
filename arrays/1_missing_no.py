# Input: nums = [3,0,1]
# Output: 2

def findmissingno(nums):
    n = len(nums)+1
    #find sum of all elements from 0 till n
    total_sum = 0
    for i in range(n):
        total_sum += i
    print(total_sum)
    #curr sum
    curr_sum = sum(nums)
    print(curr_sum)

    return total_sum - curr_sum

def findmissingno2(nums):
    for i in range(len(nums) + 1):
        if i not in nums:
            return i
        
def usingXor(nums):
    n = len(nums)

    total_sum = n * (n + 1) // 2
    curr_sum = sum(nums)
    return total_sum ^ curr_sum

def usingXor2(nums):
    ans = 0
    for i in nums:
        ans ^= i
    
    for i in range(len(nums)+1):
        ans ^= i
    
    return ans

def usingDict(nums):
    n = len(nums) + 1
    dict1 = {}
    for i in nums:
        dict1[i] = True
    print(dict1)
    for i in range(n):
        if i not in dict1:
            return i
        
nums = [0, 3, 1]
print(usingXor2(nums))
