import utility
from bnb import BnB
from sa import SimulatedAnnealing


def runBnB():
    csv_file = "bnb.csv"
    header = ["88202623", "40128045", "30009330"]
    algorithm_type = ["BnB"]
    data = []
    N = 19
    for n in range(1, N):
        adjacency_matrix = utility.write_distance_matrix(n, 0.0, 1.0)
        bnb = BnB(adjacency_matrix)
        results = bnb.run()
        data.append([results[0], results[1]])
    utility.write_into_cvs(csv_file, header, algorithm_type, data)

def cost(adjacency_matrix, path) -> float:
    path_len = 0
    for i in range(1, len(path)):
        path_len += adjacency_matrix[path[i-1]][path[i]]
    return path_len


def testBnB():
    adjacency_matrix = utility.read("15_0.0_1.0.out")
    bnb = BnB(adjacency_matrix)
    results = bnb.run()
    path = [0, 3, 9, 11, 1, 7, 2, 13, 4, 5, 14, 8, 6, 12, 10, 0]
    print(cost(adjacency_matrix, path))
    print(results)

def main():
    # Read the input file
    
    # test_matrix = [[0, 1, 3, 5, 8],
    #                [1, 0, 4, 2, 7],
    #                [3, 4, 0, 9, 2],
    #                [5, 2, 9, 0, 2],
    #                [8, 7, 2, 2, 0]]

    # results = []
    # for i in range(1):
    #     adjacency_matrix = utility.write_distance_matrix(300, 0.0, 1.0)

    #     # Create an instance of the BnB class
    #     bnb = BnB(adjacency_matrix)

    #     # Create an instance of the Simulated Annealing class
    #     sa = SimulatedAnnealing(adjacency_matrix)
    #     sa_result = sa.run()
    #     results.append(sa_result)
    #     print("sa result: {}".format(sa_result))

    # with open("results.txt", "a") as f:
    #     f.write("========================================\n")
    #     for result in results:
    #         for i in result:
    #             f.write(str(i) + "\n")
    #         f.write("========================================\n")
    # initialt = [1e-8, 1e-5, 0.0003, 0.0001, 0.003, 0.001, 0.03, 0.01]
    # final_ts = [10000, 8000, 5000, 2000, 1000, 500, 100]
    # alfas = [0.99, 0.985, 0.98, 0.97, 0.96]
    
    adjacency_matrix = utility.write_distance_matrix(30, 0.0, 1.0)
    bnb = BnB(adjacency_matrix)
    bnb_result = bnb.run()
    print("bnb result: {}".format(bnb_result))
    
    sa = SimulatedAnnealing(adjacency_matrix)
    sa_result = sa.run()
    print("sa result: {}".format(sa_result))
    # runBnB()

if __name__ == "__main__":
    main()
    