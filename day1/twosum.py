def twoSum(nums, target):
    # Store numbers you've seen
    hashmap = {}
    for i in range(len(nums)):
        compliment=target-nums[i]
        if compliment in hashmap:
            return[hashmap[compliment],i]
        hashmap [nums[i]]=i

    return []
# Example 1
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Should print [0, 1]

# Example 2
nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))  # Should print [1, 2]