# nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

def brute_(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
    return result
#problem:- repeat hot elements [[-1, 0, 1], [-1, 2, -1], [0, 1, -1]]
#we only wants one time
#if we use set it is going to delete arbirarily anyone

def two_pointer(nums):
    result = []
    nums.sort()
    for i in range(len(nums)):
        #if consecutive similar skip
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j += 1

                while nums[j] == nums[j-1] and j < k:
                    j += 1
    return result


nums = [-1,-1,0,1,2,-1,-4]
print(two_pointer(nums))