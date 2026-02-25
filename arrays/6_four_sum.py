# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

def _4sum(nums, target):
    result = []
    nums.sort()
    #this loop should at index 2 because 4 ele completed
    for i in range(len(nums)-3):
        #if cosecutive similar then skip
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        #this loop should stop at index 3 because then 4 ele completed
        for j in range(i + 1, len(nums)-2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            l = len(nums) - 1
            while k < l:
                total = nums[i] + nums[j] + nums[k] + nums[l]
                if total == target:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1

                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1
                elif total > target:
                    l -= 1
                else:
                    k += 1
    return result

nums = [1,0,-1,0,-2,2]
target = 0
print(_4sum(nums, target))