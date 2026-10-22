class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        left_size = (n + m + 1) // 2

        left, right = 0, n

        while left <= right:
            i = (left + right) // 2
            j = left_size - i

            leftA = nums1[i - 1] if i > 0 else float("-inf")
            rightA = nums1[i] if i < n else float("inf")

            leftB = nums2[j - 1] if j > 0 else float("-inf")
            rightB = nums2[j] if j < m else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if (n + m) % 2 == 1:
                    return max(leftA, leftB)

                return (max(leftA, leftB) + min(rightA, rightB)) / 2

            elif leftA > rightB:
                right = i - 1

            else:
                left = i + 1