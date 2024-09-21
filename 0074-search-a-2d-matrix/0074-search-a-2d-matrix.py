class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        l, r = 0, len(matrix)-1
        row = 0
        while (l<=r):
            m = ((r-l)//2)+l
            if (matrix[m][0]<=target and matrix[m][-1]>=target):
                row = m
                j = 0
                k = len(matrix[m])-1
                while (j<=k):
                    l = ((k-j)//2)+j
                    if (matrix[m][l]==target):
                        return True
                    elif (matrix[m][l]<target):
                        j = l+1
                    else:
                        k = l-1
                return False
            elif (matrix[m][0]<target and matrix[m][-1]<target):
                l = m+1
            else:
                r = m-1
        return False