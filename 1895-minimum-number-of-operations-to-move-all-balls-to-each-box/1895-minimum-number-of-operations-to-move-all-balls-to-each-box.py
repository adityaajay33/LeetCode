class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        '''each character is the number of balls available in that box,

        '''
        
        n = len(boxes)
        left_pass, right_pass = [], []
        balls, moves = 0, 0

        for i in range(n):
            left_pass.append(moves)

            balls+=int(boxes[i])
            moves+=balls


        balls, moves = 0, 0
        for i in range(n-1, -1, -1):
            right_pass.append(moves)

            balls+=int(boxes[i])
            moves+=balls

        right_pass.reverse()


        return [left_pass[i]+right_pass[i] for i in range(len(boxes))]
            
                
        