graph = { 
    'X': ['Y', 'Z'], 
    'Y': ['W'], 
    'Z': ['W'], 
    'W': ['V'], 
    'V': [] 
} 
visited = []
queue = [] 
def bfs(visited, graph, node):
    visited.append(node)     
    queue.append(node) 
    while queue:
        m = queue.pop(0)
        print(m, end=" ") 
        for neighbour in graph[m]:             
            if neighbour not in visited:                 
                visited.append(neighbour)                 
                queue.append(neighbour) 
print("This is the Breadth-First Search for the given graph") 
bfs(visited, graph, 'X')

