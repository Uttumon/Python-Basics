graph = {
  'A' : [('B',4),('C', 2),('D', 3)],
  'B' : [('A',4),('E', 2)],
  'C' : [('A',2),('G', 4)],
  'D' : [('A',3),('F', 3)],
  'E' : [('B',2),('F', 1)],
  'F' : [('E',1),('H', 1),('D', 3)],
  'G' : [('C',4),('H', 1)],
  'H' : [('F',1),('G', 1)],
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
            
print("Following is the Depth-First Searc+h")
dfs(visited, graph, 'A','H')