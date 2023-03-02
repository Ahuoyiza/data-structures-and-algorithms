# adjaceny list of a directional graph in python

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['D'],
    'D': ['E', 'A'],
    'E': [],
}

for key, val in graph.items():
  print(f"{key}-->{val}")