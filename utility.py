#read out file into adjacency matrix
import numpy as np
import csv

def read(out_file):
    with open(out_file, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(1, n+1):
            line = lines[i].split()
            for j in range(n):
                adjacency_matrix[i-1][j] = float(line[j])
    return adjacency_matrix


def write_distance_matrix(n, mean, sigma):
    distance_matrix = np.zeros((n, n))
    random_distance = []
    num_distance = int(n * (n-1) / 2)
    for _ in range(num_distance):
        distance = 0
        while distance <= 0:
            distance = np.random.normal(mean, sigma)

        random_distance.append(distance)
    
    iu = np.triu_indices(n, 1)
    distance_matrix[iu] = random_distance
    distance_matrix += distance_matrix.T
    np.savetxt(
        f"{n}_{mean}_{sigma}.out",
        distance_matrix,
        delimiter=" ",
        fmt="%1.4f",
        header=str(n),
        comments="",
    )
    #print(distance_matrix)
    return distance_matrix


def write_into_cvs(csv_file, header, algorithm_type, data):
    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(algorithm_type)
        for line in data:
            writer.writerow(line)

