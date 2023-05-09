#  -*- coding: utf-8 -*-
import math                        
import time
import numpy as np                 
from utility import read
class SimulatedAnnealing(object):
  def __init__(self, adjacency_matrix, alfa_i) -> None:
    self.adjacency_matrix = adjacency_matrix
    self.initial_t = 2000          # initial temperature
    self.final_t   = 0.003           # stop temperature
    self.inner_iterations = 5000     # inner loop no of iterations
    self.alfa      = alfa_i            # cooling parameter，T(k) = alfa*T(k-1)

  def cost(self, solution) -> float:
    cost = self.adjacency_matrix[solution[-1]][solution[0]]
    for i in range(len(solution) - 1):
      cost += self.adjacency_matrix[solution[i]][solution[i+1]]
    return cost

  def swap_operator(self, current_solution) -> list:
    new_solution = current_solution.copy()
    i = np.random.randint(0, len(current_solution) - 1)
    j = np.random.randint(0, len(current_solution) - 1)
    while i == j:
      j = np.random.randint(0, len(current_solution) - 1)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution
  
  def inversion_operator(self, current_solution) -> list:
    new_solution = current_solution.copy()
    i = np.random.randint(0, len(current_solution) - 1)
    j = np.random.randint(0, len(current_solution) - 1)
    while i == j:
      j = np.random.randint(0, len(current_solution) - 1)
    if i > j:
      i, j = j, i
    while i < j:
      new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
      i += 1
      j -= 1
    return new_solution
  
  def move_operator(self, current_solution) -> list:
    new_solution = list(current_solution.copy())
    i = np.random.randint(0, len(current_solution) - 1)
    j = np.random.randint(0, len(current_solution) - 1)
    while i == j:
      j = np.random.randint(0, len(current_solution) - 1)
    if i > j:
      i, j = j, i
    e = new_solution.pop(i)
    new_solution.insert(j, e)
    return new_solution

  def update_path(self, operator, current_path):
    if operator == 'swap':
      return self.swap_operator(current_path)
    elif operator == 'inversion':
      return self.inversion_operator(current_path)
    elif operator == 'move':
      return self.move_operator(current_path)
    else:
      raise Exception('No such operator')

  def simulated_annealing(self, operator) -> tuple:
    
    no_of_cities = len(self.adjacency_matrix[0])
    current_path = np.arange(no_of_cities)
    cur_len = self.cost(current_path)
    best_path = current_path.copy()
    best_len = cur_len
    iteration = 0

    best_len_track = []
    cur_len_track = []

    current_temp = self.initial_t

    while current_temp - self.final_t > 1e-10:
      for _ in range(self.inner_iterations):
        new_path = self.update_path(operator, current_path)
        new_len = self.cost(new_path)
        delta_E = new_len - cur_len

        if delta_E < 0:
          current_path = new_path
          cur_len = new_len
          if cur_len < best_len:
            best_path = current_path
            best_len = cur_len
        else:
          if np.random.randint(2) < math.exp(-delta_E / self.initial_t):
            current_path = new_path
            cur_len = new_len
      
      current_path = np.roll(current_path, 2)
      best_len_track.append(best_len)
      cur_len_track.append(cur_len)

      print('i:{}, t(i):{:.4f}, cur_len:{:.4f}, best_len:{:.4f}'.format(iteration, current_temp, cur_len, best_len))

      iteration += 1
      current_temp *= self.alfa
  
    return best_path, best_len

    
  def run(self) -> tuple:
    #operators = ['swap', 'inversion', 'move']
    operators = ['inversion']
    r = []
    for operator in operators:
      start_time = time.time()
      best_path, best_len = self.simulated_annealing(operator)
      end_time = time.time()

      best_path = np.append(best_path, best_path[0])
      r.append((operator, best_len, end_time - start_time, best_path))

    return r


if __name__ == "__main__":
  matrix = read('15_0.0_1.0.out')
  sa = SimulatedAnnealing(matrix)
  solution = [0, 10, 1, 8, 7, 12, 5, 9, 4, 11, 6, 13, 3, 2]
  print(sa.cost(solution))