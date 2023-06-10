from LogManager import LogManager
from backtracking import packaging_backtracking
from time import time
from utils import generate_packages

amount_path = "backtracking_amount_packages.txt"
times_path = "backtracking_times.txt"
solutions_path = "backtracking_solutions.txt"
solutions_len_path = "backtracking_solutions_len.txt"
log = LogManager()

def run_backtracking_tests():
    test_1_package_returns_1_container_with_the_package()
    test_2_small_packages_returns_1_container_with_the_2_packages()
    test_2_big_packages_returns_2_containers_with_1_package_each()
    test_3_small_packages_returns_1_container_with_the_3_packages()
    test_3_big_packages_returns_3_containers_with_1_package_each()
    test_4_custom_packages()
    test_given_on_the_problem_statement()
    test_of_volume()

def test_1_package_returns_1_container_with_the_package():
    packages = [1]
    expected = [[1]]
    result = packaging_backtracking(packages)
    assert result == expected

def test_2_small_packages_returns_1_container_with_the_2_packages():
    packages = [0.1, 0.1]
    expected = [[0.1, 0.1]]
    result = packaging_backtracking(packages)
    assert result == expected

def test_2_big_packages_returns_2_containers_with_1_package_each():
    packages = [1, 1]
    expected = [[1], [1]]
    result = packaging_backtracking(packages)
    assert result == expected

def test_3_small_packages_returns_1_container_with_the_3_packages():
    packages = [0.1, 0.1, 0.1]
    expected = [[0.1, 0.1, 0.1]]
    result = packaging_backtracking(packages)
    assert result == expected

def test_3_big_packages_returns_3_containers_with_1_package_each():
    packages = [1, 1, 1]
    expected = [[1], [1], [1]]
    result = packaging_backtracking(packages)
    assert result == expected

def test_4_custom_packages():
    packages = [0.25, 0.25, 0.25, 0.25, 0.25]
    expected = [[0.25, 0.25, 0.25, 0.25], [0.25]]
    result = packaging_backtracking(packages)
    assert len(result) == len(expected)
    assert result.__contains__(expected[0])
    assert result.__contains__(expected[1])

def test_given_on_the_problem_statement():
    packages = [0.4, 0.8, 0.5, 0.1, 0.7, 0.6, 0.1, 0.4, 0.2, 0.2]
    expected = [[0.1, 0.4, 0.5], [0.4, 0.6], [0.2, 0.8], [0.1, 0.2, 0.7]]
    result = packaging_backtracking(packages)
    for container in result:
        container.sort()
    assert len(result) == len(expected)
    assert result.__contains__(expected[0])
    assert result.__contains__(expected[1])
    assert result.__contains__(expected[2])
    assert result.__contains__(expected[3])

def test_of_volume():
    volumes = [i for i in range(1, 31)]
    log.new_execution(amount_path)
    log.new_execution(times_path)
    log.new_execution(solutions_path)
    log.new_execution(solutions_len_path)
    cant_ejecuciones = 5
    for amount_packages in volumes:
        print("Testing " + str(amount_packages) + " packages")
        times = []
        solutions = []
        for i in range(cant_ejecuciones):
            packages = generate_packages(amount_packages)
            start_time = time()
            solution = packaging_backtracking(packages)
            solutions.append(solution)
            end_time = time()
            time_elapsed = float("%.3f" % (end_time - start_time))
            times.append(time_elapsed)
        avg_time = float("%.3f" % (sum(times) / cant_ejecuciones))
        log.console_log(amount_packages, avg_time)
        log.log_result(amount_path, amount_packages)
        log.log_result(times_path, avg_time)
        log.log_result(solutions_path, solution)
        log.log_result(solutions_len_path, len(solution))
    log.end_line(amount_path)
    log.end_line(times_path)