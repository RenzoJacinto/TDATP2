from LogManager import LogManager
from aproximation_students import packaging_aproximation_students
from backtracking import packaging_backtracking
from aproximation import packaging_aproximation
from utils import generate_packages

comparison_path = "comparison.txt"
aproximations_comparison_path = "comparison_aprox.txt"
log = LogManager()

def run_comparison_tests():
    test_comparison()
    test_aproximations_comparison()

def test_comparison():
    volumes = [i for i in range(5, 21)]
    cant_ejecuciones = 3
    log.new_execution(comparison_path)
    for amount_packages in volumes:
        print("Testing " + str(amount_packages) + " packages")
        for i in range(cant_ejecuciones):
            packages = generate_packages(amount_packages)
            solution_backtracking = packaging_backtracking(packages)
            solution_aproximation = packaging_aproximation(packages)
            comparison = float("%.3f" % (len(solution_aproximation) / len(solution_backtracking)))
            log.log_result(comparison_path, comparison)
    log.end_line(comparison_path)

def test_aproximations_comparison():
    volumes = [i for i in range(50, 1001)]
    log.new_execution(aproximations_comparison_path)
    times_better_aproximation_statement = 0
    times_better_aproximation_students = 0
    total_iterations = len(volumes)
    for amount_packages in volumes:
        print("Testing " + str(amount_packages) + " packages")
        packages = generate_packages(amount_packages)
        solution_aproximation = packaging_aproximation(packages)
        solution_aproximation_students = packaging_aproximation_students(packages)
        comparison = float("%.3f" % (len(solution_aproximation) / len(solution_aproximation_students)))
        if (comparison > 1):
            times_better_aproximation_students += 1
        elif (comparison < 1):
            times_better_aproximation_statement += 1
        log.log_result(aproximations_comparison_path, comparison)
    log.end_line(aproximations_comparison_path)
    print("Times better aproximation statement: " + str(times_better_aproximation_statement) + " of " + str(total_iterations))
    print("Times better aproximation students: " + str(times_better_aproximation_students) + " of " + str(total_iterations))