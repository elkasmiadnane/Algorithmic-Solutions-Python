from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        mergedArray = (nums1 + nums2)
        mergedArray.sort()

        if (len(mergedArray) % 2 == 0):
            medium1 = mergedArray[int(len(mergedArray) / 2)]
            medium2 = mergedArray[int(len(mergedArray) / 2 - 1)]

            return round(float((medium1 + medium2) / 2), 4)

        else:
            if (len(mergedArray) % 2 == 1):
                return round(float(mergedArray[int(len(mergedArray) / 2)]), 4)

if __name__ == '__main__':
    solution = Solution()

    # Unit Tests

    assert (solution.findMedianSortedArrays([0,2] , [1,3]) == 1.5)
    assert (solution.findMedianSortedArrays([0, 0], [0,0]) == 0)
    assert (solution.findMedianSortedArrays([2], []) == 2)
    assert (solution.findMedianSortedArrays([1,3], [2]) == 2)


    print(' End of Tasks ')