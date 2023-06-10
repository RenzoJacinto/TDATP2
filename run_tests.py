from aproximation_tests import run_aproximation_tests
from backtracking_tests import run_backtracking_tests
from comparison_test import run_comparison_tests

def run_tests():
    run_backtracking_tests()
    run_aproximation_tests()
    run_comparison_tests()

run_tests()