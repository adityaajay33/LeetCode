class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        '''

        1 + 1, 

        '''

        answers.sort()
        prevRabbits = None
        count, matches = 0, 0

        for rabbits in answers:
            if not rabbits or rabbits!=prevRabbits or matches==0:
                count+=(rabbits+1)
                matches = rabbits
            else:
                matches -= 1 
            print(f"for rabbit {rabbits} this is the {count} and {matches}")
            
            prevRabbits = rabbits

        return count

        