class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        '''

        n students that use indexing
        each studenth is given an nth problem
        after n-1 is reached the teacher will start the process again sstarting at 0
        array chalk and integer k
        '''
        sumChalk = sum(chalk)
        remainder = k%sumChalk

        while remainder>=0:
            for i in range(len(chalk)):
                remainder -= chalk[i]

                if remainder<0:
                    return i
        
