class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        a=n-k
        if a>0:
            i=0
            while i<a:
                nums.append(nums[i])
                i+=1
            replacement=nums[a:n+a]
            nums[0:n+a]=replacement
        elif a<0:
            i=n-(k%n)
            j=0
            while j<i:
                nums.append(nums[j])
                j+=1
            replacement=nums[i:n+i]
            nums[0:n+i]=replacement
            