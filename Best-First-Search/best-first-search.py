graph = {
    'A': [('B', 2), ('C', 3), ('D', 5)],
    'B': [('E', 4), ('F', 1)],
    'C': [('G', 6), ('H', 2)],
    
    'D': [('I', 3), ('J', 4)],
    'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []
}

heuristic = {
    "A": 5, "B": 4, "C": 1, "D": 6, "E": 7,
    "F": 6, "G": 3, "H": 0, "I": 4, "J": 5
}

def best_first_search(start, goal):
    queue = [(start, 0, heuristic[start])]  # (node, cost_so_far, heuristic)
    visited = set()
    while queue:
        # sort by heuristic (greedy)
        queue.sort(key=lambda x: x[2])
        node, cost, h = queue.pop(0)
        print(node)
        if node == goal:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                queue.append((neighbor, cost + edge_cost, heuristic[neighbor]))

print("BestFS Cost:", best_first_search('A', 'H'))