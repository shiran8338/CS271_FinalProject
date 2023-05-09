#a class for branch and bound
import time

class BnB(object):
    def __init__(self, adjacency_matrix) -> None:
        self.adjacency_matrix = adjacency_matrix
        self.n = len(adjacency_matrix)
        self.best_solution = None
        self.best_cost = float('inf')
        self.visited = [False] * self.n
    

    def heuristic(self, remaining_edges, min_edge) -> float:
        return min_edge * remaining_edges


    def branchAndBound(self, current_node, remaining_edges, min_edge, current_cost, current_path) -> None:
        if current_cost + self.heuristic(remaining_edges, min_edge) >= self.best_cost:
            return

        if remaining_edges == 1:
            current_cost += self.adjacency_matrix[current_node][0]
            if current_cost < self.best_cost:
                self.best_cost = current_cost
                self.best_solution = current_path + " " + str(current_node) + " " + str(0)
            return

        for neighbor in range(1, self.n):
            if not self.visited[neighbor] and neighbor != current_node:
                self.visited[neighbor] = True
                self.branchAndBound(neighbor, remaining_edges - 1, min_edge, current_cost + self.adjacency_matrix[current_node][neighbor], current_path + " " + str(current_node))
                self.visited[neighbor] = False

    
    def run(self) -> tuple:
        start_time = time.time()
        min_edge = float('inf')
        for i in range(self.n):
            for j in range(self.n):
                if self.adjacency_matrix[i][j] != 0:
                    min_edge = min(min_edge, self.adjacency_matrix[i][j])
        self.branchAndBound(0, self.n, min_edge, 0, "")
        end_time = time.time()
        return (self.best_cost, end_time - start_time, self.best_solution)