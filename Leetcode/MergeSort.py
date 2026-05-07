class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        indexOfM=m-1
        indexOfN=n-1
        indexOfRight=m+n-1

        while indexOfN>=0:
            if indexOfM>=0 and nums1[indexOfM]>nums2[indexOfN]:
                nums1[indexOfRight]=nums1[indexOfM]
                indexOfM-=1
            else:
                nums1[indexOfRight]=nums2[indexOfN]
                indexOfN-=1
            indexOfRight-=1

