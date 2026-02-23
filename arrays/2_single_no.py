def findsingleno(nums):
    #use dictionary and store the count of each element 
    #return the element having count 1 
    #it is best suited for dictionary
    freq = {}
    for i in nums:
        #brute without any function
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    for i in freq:
        if freq[i] == 1:
            return i

def usingXor(nums):
    #best solution using xor because similar elements gets cancel out
    ans = 0
    for i in nums:
        ans ^= i
    return ans
        


nums = [4, 1, 2, 1, 2]
print(usingXor(nums))
