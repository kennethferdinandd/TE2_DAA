import math
import time 
import tracemalloc

def partition_values_from_index(values, start_index, total_value, unassigned_value, test_assignment, test_value, best_assignment, best_err):
    if start_index >= len(values):
        test_err = abs(2 * test_value - total_value)
        if test_err < best_err[0]:
            best_err[0] = test_err
            best_assignment[:] = test_assignment[:]
            print(best_err[0])
    else:
        test_err = abs(2 * test_value - total_value)
        if test_err - unassigned_value < best_err[0]:
            unassigned_value -= values[start_index]
            test_assignment[start_index] = True
            partition_values_from_index(values, start_index + 1,
                                         total_value, unassigned_value,
                                         test_assignment, test_value + values[start_index],
                                         best_assignment, best_err)

            # Try adding values[start_index] to set 2.
            test_assignment[start_index] = False
            partition_values_from_index(values, start_index + 1,
                                         total_value, unassigned_value,
                                         test_assignment, test_value,
                                         best_assignment, best_err)

with open('dataset_40_elements.txt', 'r') as file:
    values = [int(line.strip()) for line in file]

start_index = 0
total_value = sum(values)
unassigned_value = total_value
test_assignment = [False] * len(values)
test_value = 0
best_assignment = [False] * len(values)
best_err = [float('inf')]

start_time = time.time()
tracemalloc.start()

partition_values_from_index(values, start_index, total_value, unassigned_value, test_assignment, test_value, best_assignment, best_err)


end_time = time.time()
elapsed_time = (end_time - start_time) * 1000  
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Best Error:", best_err[0])
print("Best Assignment:", best_assignment)
print("Elapsed Time:", elapsed_time, "milliseconds")
print("Peak Memory Usage:", peak, "bytes")

with open('output_bnb_40_elements.txt', 'w') as file:
    file.write(f"Best Error: {best_err[0]}\n")
    file.write(f"Best Assignment: {best_assignment}\n")
    file.write(f"Elapsed Time: {elapsed_time:.6f} milliseconds\n")
    file.write(f"Peak Memory Usage: {peak:.6f} bytes\n")
