nums1 = [1, 3, 5, 7, 9]
nums2 = [-1, -2, 5, 7, 9]
nums2.extend(nums1[:3])
nums2.sort()
print(nums2)