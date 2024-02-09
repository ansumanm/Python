from collections import deque

#define the graph as an adjacency list

graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['A', 'E'],
  'D': ['B', 'E'],
  'E': ['C', 'D'] 
}

def bfs_shortest_path(graph, start, goal):
  # Keep track of explored nodes
  explored = []

  # Keep track of all the paths to be checked.
  queue = deque([[start]]) # Queue of paths

  while queue:
    # Pop the first path from the queue
    path = queue.popleft()

    # Get the last node from the path
    node = path[-1]
    if node not in explored:
      neighbours = graph[node]

      for neighbour in neighbours:
        new_path = list(path)
        new_path.append(neighbour)
        queue.append(new_path)

        if neighbour == goal:
          return new_path
    
    explored.append(node)

start = 'A'
goal = 'D'

# bfs_shortest_path(graph, start, goal)
print(f"Shortest path from {start} to {goal}: {bfs_shortest_path(graph, start, goal)}")