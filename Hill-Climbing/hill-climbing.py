graph = {
    'A': [('B', 2), ('C', 3), ('D', 5)],
    'B': [('E', 4), ('F', 1)],
    'C': [('G', 6), ('H', 2)],
    
    'D': [('I', 3), ('J', 4)],
    'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []
}

# estimated cost to reach goal (H)
heuristic = {
    "A": 5, "B": 4, "C": 1, "D": 6, "E": 7,
    "F": 6, "G": 3, "H": 0, "I": 4, "J": 5
}

def hill_climbing(start, goal):
    current = start
    total_cost = 0
    path = [current]

    while current != goal:
        neighbors = graph[current]
        if not neighbors:
            break  # stuck, no further moves

        # pick neighbor with lowest heuristic
        next_node, edge_cost = min(neighbors, key=lambda x: heuristic[x[0]])

        # stop if no improvement
        if heuristic[next_node] >= heuristic[current]:
            break

        current = next_node
        total_cost += edge_cost
        path.append(current)
        print(current)

    return total_cost

print("Hill-Climbing Cost:", hill_climbing('A', 'H'))