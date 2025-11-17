# find potimal solution using UCS algorithm

graph = {
    "A": [("B", 3), ("C", 5), ("D", 2)],
    "B": [("E", 4), ("F", 6)],
    "C": [("G", 1), ("H", 7)],
    "D": [("I", 3), ("J", 8)],
    "E": [("K", 2), ("L", 5)],
    "F": [("M", 1)],
    "G": [("N", 4)],
    "H": [("O", 3), ("P", 6)],
    "I": [("Q", 2)],
    "J": [("R", 3)],
    "K" : [],
    "L" : [],
    "M" : [],
    "N" : [],
    "O" : [],
    "P" : [],
    "Q" : [],
    "R" : [],
}

print("Adjacency list:", graph)

def ucs(start, goal):
    queue = [(start, 0)]
    visited = set()
    while queue:
        queue.sort(key=lambda x: x[1])
        node, cost = queue.pop(0)
        print(node)
        if node == goal:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                queue.append((neighbor, cost + edge_cost))

print("UCS Cost:", ucs('A', 'K'))
