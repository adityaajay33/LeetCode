from typing import List, Set, Tuple

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions are in the order: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0  # Start by facing north
        x_coord, y_coord = 0, 0  # Starting position
        obstacle_set = set(map(tuple, obstacles))  # Set of obstacles for quick lookup
        max_distance_sq = 0  # Maximum distance squared
        
        for cmd in commands:
            if cmd == -1:  # Turn right
                direction = (direction + 1) % 4
            elif cmd == -2:  # Turn left
                direction = (direction - 1) % 4
            else:
                # Move forward `cmd` steps in the current direction
                dx, dy = directions[direction]
                for step in range(cmd):
                    # Check if the next step hits an obstacle
                    if (x_coord + dx, y_coord + dy) not in obstacle_set:
                        x_coord += dx
                        y_coord += dy
                        # Update the maximum distance squared
                        max_distance_sq = max(max_distance_sq, x_coord**2 + y_coord**2)
                    else:
                        # Stop moving if an obstacle is hit
                        break
        
        return max_distance_sq