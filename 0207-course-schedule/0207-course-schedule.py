class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = {}
        for course, prereq in prerequisites:
            temp = courses.get(course, [])
            temp.append(prereq)
            courses[course] = temp

        
        visited = set()

        def dfs(c, trace):

            if c in visited or c not in courses:
                return True
            if c in trace:
                return False

            
            trace.add(c)
            for pre in courses[c]:
                ret = dfs(pre, trace)

                if not ret:
                    return False

            trace.remove(c)
            visited.add(c)
            return True
            

        for c in range(numCourses):
            out = dfs(c, set())
            if not out:
                return False

        return True
        