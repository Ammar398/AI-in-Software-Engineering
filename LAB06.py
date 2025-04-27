#Task (a): Implement Traveling Salesman Problem (TSP) in Python

from itertools import permutations

def travelling_salesman_problem(graph, start):
    vertices = list(range(len(graph)))
    vertices.remove(start)

    min_path = float('inf')
    best_permutation = None

    for perm in permutations(vertices):
        current_cost = 0
        k = start
        for j in perm:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start]

        if current_cost < min_path:
            min_path = current_cost
            best_permutation = perm

    print(f"Minimum cost Hamiltonian Cycle: {min_path}")
    print("Path:", [start] + list(best_permutation) + [start])

# Example graph
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

travelling_salesman_problem(graph, start=0)



#Task (b): Implement Tower of Hanoi in Python

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)

# Example usage
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'B', 'C')


