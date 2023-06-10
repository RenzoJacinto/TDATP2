import heapq
from utils import same_value
from copy import copy

def packaging_aproximation_students(input_packages):
    packages = copy(input_packages)
    min_heap = []
    aux = []
    for package in packages:
        package_appended = False
        while (min_heap and not package_appended):
            (remaining_size, container) = heapq.heappop(min_heap)
            if (package < remaining_size or same_value(package, remaining_size)):
                container.append(package)
                remaining_size -= package
                package_appended = True
                heapq.heappush(min_heap, (remaining_size, container))
                break
            else:
                aux.append((remaining_size, container))
        for (remaining_size, container) in aux:
            heapq.heappush(min_heap, (remaining_size, container))
        aux = []
        if (not package_appended):
            new_container = [package]
            container_size = 1.0 - package
            heapq.heappush(min_heap, (container_size, new_container))
    return min_heap