def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


# Test Cases
nums1 = [1, 2, 3, 1]
print(containsDuplicate(nums1))  # True

nums2 = [1, 2, 3, 4]
print(containsDuplicate(nums2))  # False

nums3 = [99, 99]
print(containsDuplicate(nums3))  # True