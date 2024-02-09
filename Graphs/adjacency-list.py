graph = {
  1: [2, 4],
  2: [1, 3],
  3: [2, 4],
  4: [1, 3]
}

def is_cyclic_util(vertex, visited, parent):
  visited[vertex] = True
  
  for neighbour in graph[vertex]:
    if not visited[neighbour]:
      if is_cyclic_util(neighbour, visited, vertex):
        return True
      # If an adjacent vertex is visited, and not the parent of the current vertex, then there is a cycle.
      elif neighbour != parent:
        return True
  return False

def is_cyclic(graph):
  visited = {vertex: False for vertex in graph}

  for vertex in graph:
    if not visited[vertex]:
      if is_cyclic_util(vertex, visited, -1):
        return True
  return False

contains_cycle = is_cyclic(graph)
print(f"Does the graph contain a cycle? {contains_cycle}")