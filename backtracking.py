from utils import get_combinations, get_permutations

def packaging_backtracking(packages):
    combinations = get_combinations(packages)
    indexes = [i for i in range(len(packages))]
    for combination in combinations:
        permutations = get_permutations(indexes)
        for permutation in permutations:
            solution = []
            counter = 0
            valid_solution_set = True
            for container_size in combination:
                container = []
                for i in range(container_size):
                    container.append(packages[permutation[counter]])
                    counter += 1
                if (sum(container) > 1):
                    valid_solution_set = False
                    break
                solution.append(container)
            if (valid_solution_set):
                return solution