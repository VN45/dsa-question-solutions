# nums = [2,7,11,15]
# target = 9
# Output: [0,1]
def brute_(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            sum_ = nums[i] + nums[j]
            if sum_ == target:
                return [i,j]
            
def dict_02(nums, target):
    #if you want index of element while performing any opration
    #best use case will be "dictionary"
    dictionary = {}
    for index, ele in enumerate(nums):
        result = target - ele
        if result in dictionary:
            return [dictionary[result], index]
    
        dictionary[ele] = index
        
def two_pointer(nums, target):
    # i = 0
    # j = len(nums) - 1
    # while i < j:
    #     if nums[i] + nums[j] == target:
    #         return [i, j]
    #     elif nums[i] + nums[j] > target:
    #         j -= 1
    #     elif nums[i] + nums[j] < target:
    #         i += 1
    #     else:
    #         return -1
    """This would have worked but the elements have to be sorted
    but when we sort positions of elements is changed this is the problem    
    """
    for i in range(len(nums)):
        nums[i] = (nums[i], i)
    nums.sort()
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i][0] + nums[j][0] == target:
            return [nums[i][1], nums[j][1]]
        elif nums[i][0] + nums[j][0] > target:
            j -= 1
        elif nums[i][0] + nums[j][0] < target:
            i += 1
        else:
            return -1



nums = [3, 2, 4]
target = 6
print(two_pointer(nums, target))