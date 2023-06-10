import sys
from time import time
from aproximation import packaging_aproximation
from aproximation_students import packaging_aproximation_students
from backtracking import packaging_backtracking

def calculate_solution(function, packages):
    start_time = time()
    solution = function(packages)
    end_time = time()
    amount_containers = len(solution)
    time_elapsed = str(round((end_time - start_time)*1000)) + "ms"
    return amount_containers, time_elapsed

if (len(sys.argv) != 3):
    print("Cantidad de argumentos inválida")
    exit(1)
input_file = sys.argv[2]
packages = []
try:
    with open(input_file) as f:
        amount_packages = int(f.readline().replace('\n', ''))
        f.readline()
        lines = f.readlines()
        packages = [float(line.replace('\n', '')) for line in lines]
except FileNotFoundError:
    print("El archivo no existe")
    exit(1)
type_of_solution = sys.argv[1]
if type_of_solution == "E":
    amount_containers, time_elapsed = calculate_solution(packaging_backtracking, packages)
    print("Solución Exacta: " + str(amount_containers))
    print(time_elapsed)
elif type_of_solution == "A":
    amount_containers, time_elapsed = calculate_solution(packaging_aproximation, packages)
    print("Solución Aproximada: " + str(amount_containers))
    print(time_elapsed)
elif type_of_solution == "A2":
    amount_containers, time_elapsed = calculate_solution(packaging_aproximation_students, packages)
    print("Solución Aproximada: " + str(amount_containers))
    print(time_elapsed)
else:
    print("Tipo de solución inválida")
