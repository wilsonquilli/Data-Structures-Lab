from collections import defaultdict
import heapq

#Exercise 1 - Graph Data Structure and Functions
class Graph:
    def __init__(self, directed = False):
        self.graph = {}
        self.directed = directed

    #Function that generates edges
    def generate_edges(graph):
        edges = []
        for node in graph:
            for neighbor in graph[node]:
                edges.append((node, neighbor))
        return edges
    
    #Function that finds isolated nodes
    def find_isolated_nodes(graph):
        isolated = []
        for node in graph:
            if not graph[node]:
                isolated.append(node)
        return isolated
    
    #Function that finds a paths
    def find_path(graph, start, end, path = None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for vertex in graph[start]:
            if vertex not in path:
                extended_path = Graph.find_path(graph, vertex, end, path)
                if extended_path:
                    return extended_path
        return None
    
    #Function that finds all paths
    def find_all_paths(graph, start, end, path = None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for vertex in graph[start]:
            if vertex not in path:
                extended_paths = Graph.find_all_paths(graph, vertex, end, path)
                for p in extended_paths:
                    paths.append(p)
        return paths
    
    #Function that checks if a graph is connected
    def is_connected(graph, start = None, visited = None):
        if visited is None:
            visited = set()

        vertices = list(graph.keys())
        if not start:
            start = vertices[0]

        visited.add(start)

        for vertex in graph[start]:
            if vertex not in visited:
                Graph.is_connected(graph, vertex, visited)

        return len(visited) == len(vertices)
    
#Exercise 3 - BFS, DFS, and Dijkstra's Algorithm
#BFS Function
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end = " ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

#DFS Function
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    print(start, end = " ")
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

#Dijkstra's Algorithm
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

#Sample Tests
graph = {
    "a": ['b', 'c'],
    "b": ['c', 'd'],
    "c": ['d'],
    "d": ['c'],
    "e": ['f'],
    "f": []
}

graph1 = {
    "a": ["d", "f"],
    "b": ["c"],
    "c": ["b", "c", "d", "e"],
    "d": ["a", "c"],
    "e": ["c"],
    "f": ["a"]
}

graph2 = {
    1: [(2,10), (3,15), (6,5)],
    2: [(3,7)],
    3: [(4,7), (6,10)],
    4: [(5,7)],
    5: [(6,13)],
    6: [(4,5)]
}

print("Edges of graph:", Graph.generate_edges(graph))
print("Edges of graph1:", Graph.generate_edges(graph1))

print("Isolated nodes in graph:", Graph.find_isolated_nodes(graph))
print("Isolated nodes in graph1:", Graph.find_isolated_nodes(graph1))

print("One path from a to d in graph:", Graph.find_path(graph, 'a', 'd'))
print("One path from a to c in graph1:", Graph.find_path(graph1, 'a', 'c'))

print("All paths from a to d in graph:", Graph.find_all_paths(graph, 'a', 'd'))
print("All paths from a to c in graph1:", Graph.find_all_paths(graph1, 'a', 'c'))

print("Is graph connected?", Graph.is_connected(graph))
print("Is graph1 connected?", Graph.is_connected(graph1))

print("BFS:", end=" "); bfs({k:[n for n,_ in v] for k,v in graph2.items()}, 1)
print("\nDFS:", end=" "); dfs({k:[n for n,_ in v] for k,v in graph2.items()}, 1)
print("\nDijkstra shortest paths:", dijkstra(graph2, 1))