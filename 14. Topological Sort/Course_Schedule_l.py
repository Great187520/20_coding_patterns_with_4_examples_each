class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        self.graph = collections.defaultdict(list)

        for course, prereq in prerequisites:
            self.graph[course].append(prereq)

        white = set(set.graph.keys())
        grey = set()
        black = set()

        while white:
            course = white.pop()

            if not self.dfs(course, grey, black):
                return False
        return True
    
    def dfs(self, course. grey, black):
        grey.add(course)

        for prereq in self.graph[course]:
            if prereq in black:
                continue

            if prereq in grey:
                return False
            
            if not self.dfs(prereq, grey, black):
                return False
            
        grey.remove(course)
        black.add(course)

        return True
    
    # T: 0(V + E), V = vertexes in graph (nodes), E = edges in graph (or connections between nodes)
    # S: 0(V )