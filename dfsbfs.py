from itertools import permutations
from queue import Queue

def input_graph():
    print("Enter the number of cities:")
    num_cities = int(input())

    print("Enter the adjacency matrix row by row (use space-separated values):")
    graph = []
    for _ in range(num_cities):
        row = list(map(int, input().split()))
        graph.append(row)

    return graph, num_cities

def calculate_path_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]] 
    return cost

def dfs_tsp(graph, start):
    num_cities = len(graph)
    stack = [(start, [start])]  
    min_cost = float('inf')
    best_path = None
    iterations = 0

    while stack:
        city, path = stack.pop()
        iterations += 1

        if len(path) == num_cities:  
            path_cost = calculate_path_cost(path, graph)
            if path_cost < min_cost:
                min_cost = path_cost
                best_path = path
        else:
            for next_city in range(num_cities):
                if next_city not in path:
                    stack.append((next_city, path + [next_city]))

    return best_path, min_cost, iterations

def bfs_tsp(graph, start):
    num_cities = len(graph)
    queue = Queue()
    queue.put((start, [start])) 
    min_cost = float('inf')
    best_path = None
    iterations = 0

    while not queue.empty():
        city, path = queue.get()
        iterations += 1

        if len(path) == num_cities:  
            path_cost = calculate_path_cost(path, graph)
            if path_cost < min_cost:
                min_cost = path_cost
                best_path = path
        else:
            for next_city in range(num_cities):
                if next_city not in path:
                    queue.put((next_city, path + [next_city]))

    return best_path, min_cost, iterations

def main():
    graph, num_cities = input_graph()

    print("Enter the starting city (0 to {}):".format(num_cities - 1))
    start_city = int(input())

    dfs_result = dfs_tsp(graph, start_city)
    bfs_result = bfs_tsp(graph, start_city)

    print("\nDFS Result:")
    print("Best Path:", dfs_result[0], "with Cost:", dfs_result[1], "Iterations:", dfs_result[2])

    print("\nBFS Result:")
    print("Best Path:", bfs_result[0], "with Cost:", bfs_result[1], "Iterations:", bfs_result[2])

if _name_ == "_main_":
    main()
