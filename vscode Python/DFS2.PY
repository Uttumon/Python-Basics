graph = {
    'A': {'B', 'C', 'D'},
    'B': {'A', 'E'},
    'C': {'A', 'G'},
    'D': {'A', 'F'},
    'E': {'B', 'F'},
    'F': {'E', 'H', 'D'},
    'G': {'C', 'H'},
    'H': {'F', 'G'}
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
            
print("Following is the Depth-First Searc+h")
dfs(visited, graph, 'A')