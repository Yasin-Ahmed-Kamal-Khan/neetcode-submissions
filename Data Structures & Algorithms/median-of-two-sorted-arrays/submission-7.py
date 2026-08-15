class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #[1,24,454,4242,241] [32,321,2444,12244]
        total = len(nums1) + len(nums2) 
        if total % 2 == 1:
            return self.getKth(nums1, nums2, (total + 1) / 2)
        

        return ((self.getKth(nums1, nums2, total /2)) + (self.getKth(nums1, nums2, total / 2 + 1))) / 2
        
    def getKth(self, A, B, k):
        while k != 1:
            if len(B) < len(A):
                A, B = B, A

            if len(A) == 0:
                return B[int(k)-1]

            i = int(min(len(A), k//2))
            j = int(min(len(B), k//2))


            if A[i - 1] <= B[j - 1]:
                A = A[i:]
                k -= i
            else:
                B = B[j:]
                k -= j

        if len(A) >= 1 and len(B) >= 1:
            return min(A[0], B[0])
        elif len(B) >= 1:
            return B[0]
        else:
            return A[0]

            