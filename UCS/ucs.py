# make a graph from a tree

graph = {
    "A" : [("B", 2), ("C", 3), ("D", 5)],
    "B" : [("E", 4), ("F", 1)],
    "C" : [("G", 6), ("H", 2)],
    "D" : [("I", 3), ("J", 4)],
    "E" : [],
    "F" : [],
    "G" : [],
    "H" : [],
    "I" : [],
    "J" : [],
}

def ucs(start, goal):
    queue = [(start, 0)]
    visited = set()
    while queue:
        # sort by total_cost (ascending)
        queue.sort(key=lambda x: x[1])
        node, cost = queue.pop(0)
        print(node)
        if node == goal:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                queue.append((neighbor, cost + edge_cost))

print("UCS Cost:", ucs('A', 'H'))