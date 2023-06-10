import copy
from random import uniform
from math import ceil
from itertools import permutations

def same_value(a, b):
    return abs(a - b) < 1e-6

def get_combinations_rec(target, current_sum, start, output, result):
    if current_sum == target:
        output.append(copy.copy(result))

    for i in range(start, target):
        temp_sum = current_sum + i
        if temp_sum <= target:
            result.append(i)
            get_combinations_rec(target, temp_sum, i, output, result)
            result.pop()
        else:
            return

def get_combinations(packages):
    target = len(packages)
    min_containers = ceil(sum(packages))
    output = []
    result = []
    get_combinations_rec(target, 0, 1, output, result)
    output.append([target])
    output = list(filter(lambda comb: len(comb) >= min_containers, output))
    output.sort(key=len)
    return output

def get_permutations(nums):
    for perm in permutations(nums):
        yield perm

def generate_packages(n):
    return [float("%.4f" % (uniform(0.0001, 1))) for i in range(n)]
