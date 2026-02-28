class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)-1 
        n=len(matrix[0])-1
        found=False

        l1=0
        h1=m
        l2=0
        h2=n
        r=0
        while(l1<=h1):
            m1=(l1+h1+1)//2
            if (matrix[m1][0]<=target<=matrix[m1][n]):
                r=m1
                break
            elif(target<matrix[m1][0]):
                h1=m1-1
            elif(target > matrix[m1][0]):
                l1=m1+1
        while (l2<=h2):
            m2=(l2+h2)//2
            if (target==matrix[r][m2]):
                found=True
                break
            elif (target < matrix[r][m2]):
                h2=m2-1
            elif (target > matrix[r][m2]):
                l2=m2+1
        return found

        
        
        
