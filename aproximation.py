from utils import same_value
from copy import copy

def packaging_aproximation(input_packages):
    packages = copy(input_packages)
    solution = []
    while (len(packages) > 0):
        container_size = 1.0
        container = []
        for package in packages:
            if (package < container_size or same_value(package, container_size)):
                container.append(package)
                container_size -= package
            else:
                break
        for package in container:
            packages.remove(package)
        solution.append(container)
    return solution