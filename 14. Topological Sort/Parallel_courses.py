class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}

        for node1, node2 in relations:
            graph[node1].append(node2)

        visited = {}
        def dfs(cur_node):
            if cur_node in visited:
                return visited[cur_node]
            else:
                visited[cur_node] = -1

            max_length = 1

            for end_node in graph[cur_node]:
                length = dfs(end_node)

                if length == -1:
                    return 1
                else:
                    max_length = max(length + 1, max_length)

            visited[cur_node] = max_length

            return max_length
        
        max_length = -1

        for node in graph:
            length = dfs(node)

            if length == -1:
                return -1
            else:
                max_length = max(length, max_length)

        return max_length
    
#T: 0(V + E)
#S: 0(V + E), where V = vertexes, E = edges