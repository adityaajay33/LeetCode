class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        if not prerequisites:
            return True
        
        # Build the adjacency list (hash map of courses and their prerequisites)
        coursesHashMap = {i: [] for i in range(numCourses)}
        for x, y in prerequisites:
            coursesHashMap[x].append(y)
        
        visited = set()        # Set to keep track of all visited courses
        visiting = set()       # Set to keep track of courses in the current DFS path
        
        # DFS function
        def dfs(course):
            if course in visiting:
                return False    # Found a cycle
            if course in visited:
                return True     # Already checked and no cycle
            
            # Mark this course as being visited in this path
            visiting.add(course)
            
            # Recurse on all its prerequisites
            for prereq in coursesHashMap[course]:
                if not dfs(prereq):
                    return False
            
            # Mark this course as fully visited
            visiting.remove(course)
            visited.add(course)
            
            return True
        
        # Check all courses
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True